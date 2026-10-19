#!/usr/bin/env python3
"""Consolidación, validación y chequeo de enlaces de la evidencia (frente A9).

Uso (desde la raíz del repo):
  python3 tools/validar_evidencia.py consolidar            # genera research/09_EVIDENCIAS.csv
  python3 tools/validar_evidencia.py validar [archivo]     # valida contra SCHEMA_EVIDENCIA.json
  python3 tools/validar_evidencia.py enlaces [archivo] [salida.csv]  # HTTP status por URL única

Reglas aplicadas al consolidar (todas trazadas en la columna notes con prefijo "A9:"):
  - Se leen los *_evidencia.csv de research/frentes en orden A1, A2, A3, A5A7, A8, A9.
  - Fusiones (misma URL + mismo hecho): se conserva el ID indicado y se anota el ID fusionado.
    No se renumera ningún ID.
  - published_at incompleto (YYYY o YYYY-MM) se vacía (el schema exige fecha completa) y la
    fecha parcial original se conserva en notes.
  - URL vacía en filas de inferencia: se reemplaza por un URN que identifica la inferencia.
  - Ajustes de confirmation_status por auditoría: diccionario AJUSTES.
"""
import csv
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parent.parent
FRENTES = RAIZ / "research" / "frentes"
SALIDA = RAIZ / "research" / "09_EVIDENCIAS.csv"
SCHEMA = RAIZ / "SCHEMA_EVIDENCIA.json"
FUENTES = ["A1_evidencia.csv", "A2_evidencia.csv", "A3_evidencia.csv",
           "A5A7_evidencia.csv", "A8_evidencia.csv", "A9_evidencia.csv"]
CAMPOS = ["id", "claim", "url", "publisher", "published_at", "accessed_at",
          "type", "confidence", "notes", "confirmation_status"]
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# ID eliminado -> ID conservado (misma URL y mismo hecho)
FUSIONES = {
    "E3041": "E1002",  # Metro Futuro en registro PSAV (mismo listado CNV, mismo hecho)
    "E5001": "E2014",  # Wefunder 7,9% + cargo anual (misma página de ayuda)
    "E5004": "E2016",  # Republic 2,5% al inversor (misma reseña)
    "E5011": "E8005",  # RG 1125 topes (misma noticia oficial); ambigüedad resuelta por E3013/E9005
    "E5007": "E2002",  # Brickken plans (misma página); E5007 tenía un error (Enterprise "a medida")
}

# Ajustes de auditoría: id -> (nuevo_status o None, nota)
AJUSTES = {
    "E1002": (None, "Re-verificado en descarga propia (E9010). Tensión regulatoria: registrado sin cat. 5 pero opera plataforma con proyectos de terceros (E9002, E9022). Hipótesis para abogado"),
    "E1012": (None, "Contenido de la nota re-leído y confirmado (E9015). Resolución aún sin cotejo en AIF"),
    "E1014": ("contradictorio", "A1 lo presenta como recaudado en la última emisión y A8 (E8011) como emisión previa no tokenizada. La fuente no dice si fue tokenizada. PAGBAM menciona 9 UF y Lexlatin 10 (E9015)"),
    "E1016": (None, "Contenido re-leído y confirmado (E9014)"),
    "E1026": (None, "El CUIT del sitio no supera el dígito verificador (E9012)"),
    "E1037": ("verificado", "Texto normativo leído en B.O. por A3 (E3012) y por A9 (E9005)"),
    "E1007": (None, "Inconsistente con E1006 (18 proyectos fondeados listados vs +76 propiedades declaradas). Unidades distintas o cifra de marketing"),
    "E2002": (None, "Re-verificado (E9020): Enterprise EUR 1.999/mes o 22.000/año"),
    "E2015": (None, "URL FINRA y AWC devuelven 403 a A9 (antibot). Contenido confirmado vía Goodwin (E9017)"),
    "E2025": (None, "Re-verificado (E9016): ~USD 140 M en la nota. No figura USD 94 M"),
    "E2031": (None, "Hay 4 registros sin situación (89+48+7+6=150 de 154). Cancelación 31,2% sobre 154 o 35,0% sobre las 137 que obtuvieron registro (E9018)"),
    "E3013": (None, "Re-verificado (E9005): el tope es por inversor"),
    "E3018": (None, "Re-verificado (E9006, E9007). Tras el sandbox no se admiten nuevas emisiones digitales"),
    "E3019": (None, "Re-verificado (E9004)"),
    "E3024": (None, "Re-verificado (E9001)"),
    "E3025": (None, "Re-verificado (E9003)"),
    "E3027": (None, "Re-verificado (E9002)"),
    "E3040": ("contradictorio", "Recuento A9: 34 con las cinco actividades. 37 es la cantidad con cat. 5 (participación en oferta de emisor) (E9011)"),
    "E5016": (None, "Recalculado por A9 sobre el prospecto (E9019)"),
    "E5024": (None, "Re-verificado (E9013)"),
    "E8001": ("verificado", "Cifras idénticas al informe CNV primario (E5024, E9013)"),
    "E8002": (None, "Resolución A9: prevalece la cifra oficial CNV (E5024). Diferencia de 2,6% por metodología y tipo de cambio de BCSF"),
    "E8005": (None, "Re-verificado (E9005). Absorbe E5011"),
    "E8006": ("verificado", "Valor confirmado en API BCRA (E5043, E9021)"),
    "E8011": ("contradictorio", "La afirmación de las notes (USD 4,15 M = emisión previa no tokenizada) no está en la fuente (E9015). El informe A8 generaliza 'no hay monto tokenizado colocado' sin considerar Landtoken I (E1016, E9014)"),
    "E8015": (None, "Outlier (E2025, E9016) da ~USD 140 M y no USD 94 M: la contradicción no se reproduce en esa nota. Escrow solo en Crypto Briefing"),
    "E8040": (None, "Dato 2024. Al 19/10/2026 hay 80 PJ con matrículas hasta 173 (E9010): no es contradicción, refleja bajas"),
}

URN_INFERENCIA = {"E8044": "urn:a8:inferencia:E8044", "E8045": "urn:a8:inferencia:E8045"}


def leer(path):
    filas = []
    with open(path, encoding="utf-8", newline="") as fh:
        lineas = fh.read().splitlines()
    if lineas[0].split(";") != CAMPOS:
        raise SystemExit(f"Encabezado inesperado en {path}")
    for n, linea in enumerate(lineas[1:], 2):
        if not linea.strip():
            continue
        partes = linea.split(";")
        if len(partes) != len(CAMPOS):
            raise SystemExit(f"{path}:{n} tiene {len(partes)} campos (se esperan 10)")
        fila = dict(zip(CAMPOS, partes))
        fila["_origen"] = f"{path.name}:{n}"
        filas.append(fila)
    return filas


def agregar_nota(fila, nota):
    base = fila["notes"].strip()
    fila["notes"] = (base + (". " if base and not base.endswith(".") else " " if base else "") + "A9: " + nota).strip()


def consolidar():
    filas = []
    for nombre in FUENTES:
        filas.extend(leer(FRENTES / nombre))
    por_id = {}
    for f in filas:
        if f["id"] in por_id:
            raise SystemExit(f"ID duplicado {f['id']} en {f['_origen']} y {por_id[f['id']]['_origen']}")
        por_id[f["id"]] = f
    # fusiones
    for quitar, conservar in FUSIONES.items():
        a, b = por_id[quitar], por_id[conservar]
        if a["url"] != b["url"]:
            raise SystemExit(f"Fusión {quitar}->{conservar} con URLs distintas")
        agregar_nota(b, f"fusionado con {quitar} (misma URL y hecho; claim de {quitar}: {a['claim'][:160]})")
    filas = [f for f in filas if f["id"] not in FUSIONES]
    for f in filas:
        if f["id"] in URN_INFERENCIA and not f["url"]:
            f["url"] = URN_INFERENCIA[f["id"]]
            agregar_nota(f, "URL vacía en origen (inferencia sin fuente propia). Se asigna URN identificador")
        pa = f["published_at"]
        if pa and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", pa):
            agregar_nota(f, f"published_at parcial en origen ({pa}). Se vacía por formato date del schema")
            f["published_at"] = ""
        if f["id"] in AJUSTES:
            estado, nota = AJUSTES[f["id"]]
            if estado and estado != f["confirmation_status"]:
                nota = f"status {f['confirmation_status']} -> {estado}. " + nota
                f["confirmation_status"] = estado
            agregar_nota(f, nota)
        for c in CAMPOS:
            f[c] = f[c].replace(";", ",").replace("\n", " ")
    with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        fh.write(";".join(CAMPOS) + "\n")
        for f in filas:
            fh.write(";".join(f[c] for c in CAMPOS) + "\n")
    print(f"{len(filas)} filas escritas en {SALIDA} ({len(FUSIONES)} fusiones)")


def validar(path=SALIDA):
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    props = schema["properties"]
    patron_id = re.compile(props["id"]["pattern"])
    enums = {k: set(v["enum"]) for k, v in props.items() if "enum" in v}
    errores, vistos = [], set()
    path = Path(path)
    for f in leer(path):
        e = lambda m: errores.append(f"{f['_origen']} {f['id']}: {m}")
        if not patron_id.fullmatch(f["id"]):
            e("id no cumple patrón")
        if f["id"] in vistos:
            e("id duplicado")
        vistos.add(f["id"])
        for req in schema["required"]:
            if not f.get(req, "").strip():
                e(f"campo requerido vacío: {req}")
        if len(f["claim"]) < props["claim"]["minLength"]:
            e("claim < 10 caracteres")
        u = urlparse(f["url"])
        if not ((u.scheme in ("http", "https") and u.netloc) or (u.scheme == "urn" and u.path)):
            e(f"url no es URI válida: {f['url']!r}")
        if f["published_at"]:
            try:
                date.fromisoformat(f["published_at"])
            except ValueError:
                e(f"published_at no es fecha completa: {f['published_at']}")
        try:
            dt = datetime.fromisoformat(f["accessed_at"])
            if dt.tzinfo is None:
                e("accessed_at sin zona horaria")
        except ValueError:
            e(f"accessed_at inválido: {f['accessed_at']}")
        for campo, valores in enums.items():
            if f[campo] not in valores:
                e(f"{campo} fuera de enum: {f[campo]}")
    print(f"{path}: {len(vistos)} filas, {len(errores)} errores")
    for x in errores:
        print("  ", x)
    return not errores


def status_url(url):
    try:
        out = subprocess.run(
            ["curl", "-sSL", "-o", "/dev/null", "-m", "20", "-A", UA,
             "-w", "%{http_code} %{url_effective}", url],
            capture_output=True, text=True, timeout=40)
        partes = out.stdout.strip().split(" ", 1)
        codigo = partes[0] if partes and partes[0] else "000"
        efectiva = partes[1] if len(partes) > 1 else ""
        err = out.stderr.strip().replace(";", ",")[:120]
        return url, codigo, efectiva, err
    except subprocess.TimeoutExpired:
        return url, "000", "", "timeout"


def enlaces(path=SALIDA, salida=None):
    urls = sorted({f["url"] for f in leer(Path(path)) if f["url"].startswith("http")})
    with ThreadPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(status_url, urls))
    salida = Path(salida) if salida else None
    lineas = ["url;http_status;url_efectiva;error"] + [";".join(r) for r in res]
    if salida:
        salida.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    else:
        print("\n".join(lineas))
    malos = [r for r in res if not r[1].startswith(("2", "3"))]
    print(f"{len(urls)} URL únicas, {len(malos)} con status no 2xx/3xx", file=sys.stderr)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validar"
    if cmd == "consolidar":
        consolidar()
        sys.exit(0 if validar(SALIDA) else 1)
    elif cmd == "validar":
        sys.exit(0 if validar(sys.argv[2] if len(sys.argv) > 2 else SALIDA) else 1)
    elif cmd == "enlaces":
        enlaces(sys.argv[2] if len(sys.argv) > 2 else SALIDA, sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        raise SystemExit(__doc__)
