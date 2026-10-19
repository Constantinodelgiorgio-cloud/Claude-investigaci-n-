# A9 — Auditoría independiente de evidencia y QA

**Fecha de ejecución:** 2026-10-19 (Argentina, 04:45–05:05 -03:00 según el reloj del entorno) · **Frente:** A9
**Entregables:** `research/09_EVIDENCIAS.csv` (253 filas, 0 errores de schema), `tools/validar_evidencia.py`, `research/frentes/A9_evidencia.csv` (E9001–E9024), este informe.
**Método:** relectura propia de las fuentes. A9 descargó de nuevo el registro PSAV, las RG 1125/1150/1172, el Tít. XXII, la Ley 26.831, el Cap. PFC, el informe anual CNV 2025, el dataset CVM y el prospecto del FF Total Assets V en una carpeta propia. No reutilizó las copias de otros frentes. También usó WebFetch/WebSearch y el chequeo HTTP de las 178 URL únicas. No se enviaron formularios ni se contactó a terceros. No hubo commits.

> Convención: **confirmado** = A9 lo leyó en la fuente y coincide. **corregido** = la fuente dice algo distinto de lo que informó el frente. **no reproducible** = A9 no pudo leer la fuente o la fuente no contiene lo que se afirma.

---

## 1. Resumen

1. **El núcleo regulatorio es robusto.** Las 9 afirmaciones regulatorias críticas del dictamen `03` se confirmaron en texto oficial: RG 1172 arts. 9, 35 y 38; Tít. XXII art. 7; RG 1125 art. 148; RG 1150 arts. 5 e), 14 y 38; Ley 26.831 art. 2; PFC arts. 45, 55 y 56. No hubo que corregir ninguna.
2. **Se resolvió la duda de los topes de la RG 1125:** son **por inversor** (el título del art. 148 es "LÍMITES POR INVERSOR"): UVA 3.000 por emisión y UVA 10.000 en el total del régimen. Quedan desactualizados A5 §1.2, la fila E5011 y la nota de la hoja `Supuestos` del 05 ("sujeto del tope a confirmar").
3. **Hubo correcciones de hecho:**
   - (a) A3 dice que 37 PSAV tienen las cinco actividades. Son **34**; 37 es la cantidad con la cat. 5.
   - (b) A8 dice que Outlier informa USD 94 M para RealT. La nota de Outlier dice **~USD 140 M**.
   - (c) A5 describe el plan Enterprise de Brickken "a medida". En realidad cuesta **EUR 1.999/mes**, y "Silver/Gold" son planes **API**, no marketplace white label.
   - (d) La tasa de cancelación CVM de 31% (48/154) es **35,0%** si se calcula sobre las 137 plataformas que alguna vez obtuvieron registro. Además hay 4 registros sin situación.
4. **Hay contradicciones relevantes entre frentes, hoy sin resolver con fuente:**
   - El monto de Illa Belgrano: A1 dice "recaudado" y A8 dice "previo no tokenizado". La fuente no sostiene ninguna de las dos.
   - A8 dice que "no hay monto tokenizado colocado". A1 documenta Landtoken I con oferta pública.
   - A1 presenta a Volsmart como "único tokenizador local con emisiones en sandbox". Justoken generó los CP digitales de Landtoken I.
5. **Calidad formal:** 35 filas de los frentes violaban el schema. Eran 33 con `published_at` parcial y 2 con URL vacía (A8). Se normalizaron en 09 sin cambiar contenido. Además, **188 de 253 filas tienen `accessed_at` posterior al reloj real de la sesión** (por ejemplo, 10:00–14:10 -03:00, cuando la sesión terminó antes de las 05:05 -03:00). Las horas de acceso de A1, A2, A5/A7 y A8 son nominales y no reales.
6. **Veredicto:** las conclusiones de **barreras regulatorias** y **"el token no aporta derechos ni liquidez"** son robustas. Las de **tamaño de oferta tokenizada local**, **costos de estructuración**, **CAC/conversión** y **uso histórico de PFC** son frágiles: dependen de fuentes secundarias, de inferencias por ausencia o de supuestos sin ancla.

---

## 2. Consolidación de `09_EVIDENCIAS.csv`

| Concepto | Valor |
|---|---|
| Filas de entrada | A1 43 · A2 52 · A3 50 · A5/A7 43 · A8 46 · A9 24 = 258 |
| Fusiones (misma URL + mismo hecho) | 5: E3041→E1002, E5001→E2014, E5004→E2016, E5011→E8005, E5007→E2002 (anotadas en `notes`, IDs no renumerados) |
| Filas en 09 | 253 (149 verificado · 68 pendiente · 23 no_verificable · 13 contradictorio) |
| Errores de schema en origen | A1 2, A2 11, A3 0, A5A7 6, A8 16, A9 0 |
| Normalizaciones aplicadas | `published_at` parcial (YYYY o YYYY-MM) → vacío, con la fecha original en `notes`. E8044/E8045 sin URL → `urn:a8:inferencia:<id>` |
| Cambios de `confirmation_status` | E1014 → contradictorio · E3040 → contradictorio · E8011 → contradictorio · E1037 → verificado · E8001 → verificado · E8006 → verificado |
| Validación final | `python3 tools/validar_evidencia.py validar` → 253 filas, 0 errores |

Reproducir: `python3 tools/validar_evidencia.py consolidar` (regenera y valida) y `python3 tools/validar_evidencia.py enlaces research/09_EVIDENCIAS.csv salida.csv`.

**Filas que no se fusionaron a propósito:**
- E1001/E3040: E3040 tiene un dato erróneo propio (el 37).
- E1012/E8011: E8011 agrega una afirmación distinta.
- E5032/E8007: URL distinta.
- E1005/E3044: hechos distintos.

---

## 3. Re-verificaciones independientes (24 afirmaciones)

| # | Afirmación (frente, ID) | Fuente re-leída | Resultado | Detalle A9 (ID) |
|---|---|---|---|---|
| 1 | RG 1172 art. 38: PSAV no puede hacer oferta pública de AV que sean VN sin autorización CNV (A3 E3024; 03) | PDF RESGC-2026-1172 en cnv.gov.ar | **confirmado** | Texto literal coincide. La fecha en el B.O. sigue sin poder reproducirse en fuente oficial (E9001, E9023) |
| 2 | RG 1172 art. 9: cat. 5 y "mero acto de emitir" (A3 E3027) | ídem | **confirmado** | Es clave para Metro Futuro (ver §5.1) (E9002) |
| 3 | RG 1172 art. 35: referenciamiento (A3 E3025) | ídem | **confirmado** | Convenio informado vía AIF en 5 días (E9003) |
| 4 | Tít. XXII art. 7: el token no crea un nuevo VN (A3 E3019) | consolidado argentina.gob.ar | **confirmado** | Agrega el ticker con sufijo "RD" (E9004) |
| 5 | RG 1125 topes UVA 3.000/10.000: ¿por inversor o por emisión? (A3 E3013, A5 E5011, A8 E8005) | PDF B.O. 07/04/2026 | **confirmado: por inversor** | Art. 148 "LÍMITES POR INVERSOR". Resuelve la ambigüedad de A5 (E9005) |
| 6 | RG 1150: sandbox hasta 31/12/2027 (A3 E3018, A5 E5032, A8 E8007) | texto RG 1150 | **confirmado y ampliado** | Art. 38: después de esa fecha **no se pueden hacer nuevas emisiones digitales**. Las existentes siguen válidas (E9006) |
| 7 | RG 1150: máximo 5 PSAV y PSAV en todas las categorías (A3 E3017) | ídem | **confirmado** | El límite está en el art. 5 e). Ese artículo tampoco exige cotizar en un mercado (E9007) |
| 8 | Ley 26.831 art. 2: definición amplia de oferta pública y de VN (A3 E3001–E3002) | texto actualizado Infoleg | **confirmado** | (E9008) |
| 9 | PFC: UVA 1,5 M por proyecto, menor entre 10% y UVA 150.000, 20% de ingresos brutos (A3 E3033, A5 E5009–E5010) | Tít. XIV Cap. I | **confirmado** | Para calificados: 20% sin tope UVA (E9009) |
| 10 | Registro PSAV: Metro Futuro, Volsmart, Efaysto y Token ByU (A1, A3) | descarga propia del xlsx CNV | **confirmado** | Metro Futuro: 3 actividades (sin custodia ni cat. 5). Volsmart (85), Efaysto (172) y Token ByU (173, CUIT 30719245982): 5 actividades cada uno (E9010) |
| 11 | "37 PSAV con las cinco actividades" (A3 E3040, A3 §4) | ídem | **corregido** | 34 tienen las cinco; 37 tienen la cat. 5; 57 tienen custodia (E9011) |
| 12 | CUIT de Token ByU en buildingtok.com (A1 E1026) | buildingtok.com + cálculo | **confirmado (contradicción real)** | El sitio dice "BUILDINTOK S.A.S. CUIT 30-71234567-8", que **no supera el dígito verificador**. El CUIT de CNV sí lo supera (E9012) |
| 13 | CNV 2025: USD 10.480 M pyme, 128 FF por USD 1.990 M (A5 E5024, A8 E8001) | PDF informe anual CNV | **confirmado** | (E9013) |
| 14 | Landtoken I: VN USD 4.777.518, USD 2.192.500 en especie, Allaria, Justoken (A1 E1016) | abogados.com.ar 29/12/2025 | **confirmado (fuente secundaria)** | La nota no da el número de resolución CNV. El efectivo de terceros sería USD 2,59 M si se integró todo (E9014) |
| 15 | Illa Belgrano: RESFC-2026-23510 y USD 4.150.330 (A1 E1012/E1014, A8 E8011) | PAGBAM y Lexlatin | **parcial / no reproducible** | La RESFC y la fecha de AIF (20/05/2026) se confirman. PAGBAM menciona 9 UF y Lexlatin 10. **Ninguna fuente dice si los USD 4,15 M fueron tokenizados** (E9015) |
| 16 | RealT: liquidación del 02/07/2026, ~USD 140 M, fiduciario (A2 E2025, A8 E8015) | Outlier Media 16/07/2026 | **confirmado; A8 corregido** | Outlier dice ~USD 140 M y no menciona USD 94 M ni escrow (E9016) |
| 17 | Multas FINRA 2022: Wefunder USD 1,4 M y StartEngine USD 350.000 (A2 E2015) | finra.org (403) → Goodwin y búsqueda | **confirmado** | Incluye el contador de inversores inflado de StartEngine (E9017) |
| 18 | CVM: 48/154 plataformas canceladas (A2 E2031) | dataset CVM descargado | **confirmado con matiz** | Hay 4 registros sin situación. La cancelación es 35,0% sobre las que obtuvieron registro (E9018) |
| 19 | FF Total Assets V: gastos 2,18% del VN (A5 E5016) | adenda del prospecto | **confirmado** | Desglose recalculado (§6) (E9019) |
| 20 | Brickken: precios (A2 E2002 vs A5 E5007) | brickken.com/plans | **A2 confirmado; A5 corregido** | Enterprise EUR 1.999/mes. Silver/Gold son API (E9020) |
| 21 | UVA y tipo de cambio BCRA (A5 E5043, A8 E8006) | API BCRA v4.0 | **confirmado** | UVA 2.159,10 (19/10) y 2.156,58 (15/10). Mayorista 1.514,5655 (16/10) (E9021) |
| 22 | Metro Futuro: 9 proyectos y leyenda PSAV (A1 E1003/E1004, A3 E3042) | metro-futuro.com/proyectos | **confirmado** | Hay desarrolladores de terceros y la web no nombra al emisor de los tokens (E9022) |
| 23 | Raíz: cifras inconsistentes y sin mercado público (A1 E1021) | raiz.finance (WebFetch) | **confirmado** | Además, la FAQ ofrece vender "en el mercado de la plataforma", lo que contradice su propio disclaimer (E9024) |
| 24 | Fecha de la RG 1172 en el B.O. (15/10/2026) (A3 E3030) | búsqueda en boletinoficial.gob.ar | **no reproducible** | Solo fuentes secundarias (E9023) |

---

## 4. Enlaces (chequeo HTTP de 178 URL únicas, curl -L, timeout 20 s, User-Agent de navegador)

Resultado: 152 con 200 · 22 con 403 · 1 con 410 · 1 con 429 · 2 sin respuesta. **Ningún `confirmation_status` cambió solo por un 403.** Detalle crudo en el scratchpad de la sesión (`enlaces.csv`).

| URL (IDs) | Status | Lectura A9 |
|---|---|---|
| regional-front.cointelegraph.com/…tzero-continues-to-lose-money (E8019) | **410 Gone** | **Roto real.** E8019 ya estaba como pendiente. Reemplazar por el 10-Q de Overstock |
| raiz.finance (E1021) | 000 (reset TLS con curl) | Bloqueo del entorno. WebFetch carga bien (E9024) |
| boletinoficial.gob.ar/detalleAviso/…/337165/20260107?anexos=1 (E5012–E5015) | 000 la primera vez, 200 al reintentar | Inestable, no roto |
| 4pillars.io (E5036) | 429 → redirige a research.4pillars.io | Rate limit. Conviene actualizar la URL a la redirigida |
| sec.gov/Archives (E5003, E5005, E2022, E8020) | 403 | La SEC exige un User-Agent con contacto. Es una política de acceso, no un enlace roto |
| finra.org (E2010, E2015) | 403 | Antibot. Contenido de E2015 confirmado por otra vía (E9017). E2010 sin re-verificar |
| outliermedia.org (E2025) | 403 con curl, 200 con WebFetch | Antibot |
| bridgedetroit.com (E2024, E8014), theblock.co (E8017, E8018, E8021), criptonoticias.com (E1018, E1040), benzinga.com (E8026), thedefiant.io (E2027), businesswire.com (E2018), republic.com (E2049), acionista.com.br (E8037), cnbsp.org.br (E2040), misq.umn.edu (E8035), github.com/ethereum/EIPs/issues/1411 (E5034) | 403 | Antibot o bloqueo regional. Contenido no re-verificado por A9. Status sin cambios |

Redirecciones verificadas: realt.co → realtusa.pulse.is (coincide con E2026).

---

## 5. Contradicciones entre frentes y resolución

| # | Contradicción | Frentes / IDs | Resolución A9 | Status en 09 |
|---|---|---|---|---|
| 5.1 | A1 dice que Metro Futuro "vende tokens propios igual". A3 dice que el registro es solo intercambio y transferencia | A1 §5, E1002, E3041, E9022 | **No es una contradicción de hechos:** las dos cosas son ciertas. La web lista proyectos de **desarrolladores terceros** (HQ y Asociados, APMB, HA Emprendimientos) y no nombra al emisor del token. Según la RG 1172 art. 9, "el mero acto de emitir" no exige la cat. 5. Pero **prestar plataforma a emisores para su oferta inicial sí es cat. 5**, y Metro Futuro no la tiene. Queda una **tensión regulatoria**, que debe tratarse como **hipótesis para abogado**, no como infracción. A1 debería escribir "opera una plataforma que ofrece tokens de proyectos propios y de terceros" | E1002 verificado (con nota) |
| 5.2 | Financiamiento 2025: CNV USD 33.679 M / pyme 10.480 M frente a BCSF USD 32.978 M / pyme 10.212 M | A5 E5024, A8 E8001/E8002 | Usar **CNV como cifra oficial** (re-verificada, E9013). BCSF usa otra metodología y otro tipo de cambio (−2,6% en pyme). A8 debe quitar la etiqueta "H/D" y citar CNV | E8001 → verificado · E8002 contradictorio |
| 5.3 | Topes RG 1125: A3/A8 los leen "por inversor" y A5 los considera "ambiguos" | E3013, E8005, E5011 | **Por inversor** (art. 148, E9005) | E5011 fusionada en E8005 |
| 5.4 | Token ByU: CUIT 30719245982 (CNV) frente a 30-71234567-8 (sitio) | E1025, E1026 | El CUIT del sitio no supera el dígito verificador y la forma societaria no coincide (S.A. frente a S.A.S.). Se mantiene como **contradictorio**, con alerta de calidad del sitio | E1026 contradictorio |
| 5.5 | Crowdium: "fideicomisos privados" (A1) frente a "fideicomisos ordinarios" (A3). CFA "inscripta" (mapa y Ámbito E5008) frente a "no verificada" (A3 E3044). 18 proyectos fondeados frente a "+76 propiedades" | E1005, E1006, E1007, E3044, E5008 | "Privado" y "ordinario" son **compatibles**: fideicomiso ordinario sin oferta pública. La inscripción de CFA como fiduciario financiero es **declarada y no verificada en registro oficial** (el registro de fiduciarios no fue consultado; queda pendiente). "Propiedades" y "proyectos" son unidades distintas: no usar 76 | E1007 no_verificable (con nota) |
| 5.6 | Cantidad de actores: A1 cuenta 18 en el mapa y "unas 6 comparables". A2 cuenta 15 modelos | A1, 02, 10 | **Consistente:** 00 y 10 repiten 18/6 y el mapa tiene exactamente 18 filas. A2 supera el mínimo de 10. El "unas 6" es juicio de A1 y debería decirse así | — |
| 5.7 | Illa Belgrano USD 4.150.330: A1 lo presenta como "recaudado en la última emisión". A8 dice "emisión previa no tokenizada" | E1014, E8011, mapa (fila Volsmart) | **No reproducible:** Lexlatin no dice si la emisión fue tokenizada y PAGBAM no da montos. Además hay 9 o 10 UF según la fuente. Hay que cotejar en la AIF | E1014 y E8011 → contradictorio |
| 5.8 | A8: "no se encontró ningún caso argentino con monto tokenizado colocado y público bajo el régimen CNV" (§0.2 y R12). A1: Landtoken I FF con oferta pública, VN USD 4,78 M, CP digitales de Justoken | A8 l.15 y l.95; E1016, E5037, E5038, E9014 | **Las dos son parcialmente ciertas:** sí hay emisiones con oferta pública y representación digital autorizada (Landtoken I, Illa Belgrano, Espacio Añelo). Lo que **no** es público es el monto efectivamente representado en tokens, porque la representación es opcional a pedido del inversor. Redacción sugerida para A8: "hay 3 FF con oferta pública y representación digital autorizada; el monto efectivamente tokenizado no está publicado" | E8011 contradictorio |
| 5.9 | A1: Volsmart es "el único tokenizador local con emisiones bajo sandbox CNV identificadas (2)". A5/A7: Justoken (Tech Demeter) generó los CP digitales de Landtoken I, presentado como "primer FF tokenizado aprobado por la CNV" | A1 l.85; E5037, E5038, E1016 | **Contradicción interna de A1:** hay al menos 2 entidades generadoras (Volsmart y Tech Demeter/Justoken). Corregir A1 | — |
| 5.10 | RealT: USD 140 M (A2, Outlier) frente a USD 94 M "según Outlier" (A8) | E2025, E8015, A8 l.88 y l.136 | **Corregido:** Outlier dice ~USD 140 M (E9016). El dato de USD 94 M no tiene fuente localizada. El escrow de USD 640 mil solo aparece en Crypto Briefing | E8015 se mantiene contradictorio (con nota) |
| 5.11 | Ritmo normativo: A7 dice "5 cambios en 15 meses" y A8 "≥10 RG en ~30 meses" | A7 l.60, A8 l.71 | Son alcances distintos (solo tokenización frente a todo el perímetro PSAV/PFC/tokenización). De RG 1069 (jun-2025) a RG 1172 (oct-2026) pasaron 16 meses. Armonizar la redacción | — |
| 5.12 | Registro PSAV: 101 inscriptos en 2024 (iProUP, E8040) frente a 80 PJ en 2026 | E8040, E9010 | No hay contradicción: las matrículas llegan a 173 con 80 vigentes, lo que indica bajas | E8040 pendiente (con nota) |

---

## 6. Aritmética recalculada

| Cálculo | Frente | Recalculado A9 | Estado |
|---|---|---|---|
| UVA 3.000 × 2.159,10 ÷ 1.514,57 | A5, 00, 10 | ARS 6.477.300 = **USD 4.277** (≈4.300) | OK |
| UVA 10.000 | A5 | ARS 21.591.000 = USD 14.256 (≈14.300) | OK |
| UVA 3.000 / 10.000 con UVA 2.156,58 | A8 | ARS 6,47 M / 21,57 M | OK |
| UVA 1.500.000 (tope PFC) | A5, 00, 10 | ARS 3.238,65 M = **USD 2,138 M** | OK |
| UVA 150.000 / 65.350 | A5 | USD 213,8 mil / USD 93,2 mil | OK |
| Tasas CNV en USD (2.805.000 / 5.611.000 / 13.360.000 / 5.344.000) | A5 | 1.852 / 3.705 / 8.821 / 3.528 | OK |
| FF Total Assets V: gastos sin impuestos | A5 E5016 | 411.162.611 ÷ 18.835.864.000 = **2,183%**. Colocación 0,887%, fiduciario 0,437%, administrador 0,377%, auditoría 0,136%, asesor 0,163%, CNV/CVA/BYMA/MAE 0,161%, otros 0,022%. Con IIBB e IVA: 2.272.074.010 = **12,06%** (IIBB solo: 9,64%) | OK |
| CVM: plataformas canceladas | A2 E2031 | 48/154 = 31,2%. 48/150 (con situación) = 32,0%. **48/137 (alguna vez registradas) = 35,0%** | Matizar |
| Promedio por FF 2025 | A5 | USD 1.990 M ÷ 128 = USD 15,5 M | OK |
| Crowdium: promedio por proyecto fondeado | A1 | 13.805.350 ÷ 18 = USD 767 mil (A1 escribe "~20 proyectos" en l.100: son 18) | Corregir "~20" |
| Landtoken I: efectivo de terceros | A1 | 4.777.518 − 2.192.500 = USD 2.585.018 (si se integró el primer tramo completo) | Inferencia A9 |
| CAC por inversor activo | A5 | 15/0,30 = 50 · 40/0,15 = 267 · 100/0,05 = 2.000 | OK |
| Umbral A5 §3 | A5 | 350.000 ÷ 0,07 = USD 5,0 M de GMV. ÷ 800 = 6.250 suscripciones. × 267 = USD 1,67 M | OK |
| M2 base, contribución por USD de GMV (05) | 05, 10 | 0,07 − [(267+1,4+6)/(800×2) + (4.000+3.000)/400.000 + 0,0025] = 0,07 − 0,1915 = **−12,15%** | OK (coincide con 10) |
| M1 base, contribución por campaña (05) | 05, 00, 10 | 400.000×2,5% + 4.000 − 4.000 − 3.000 − 400.000×0,25%/2 = **USD 6.500**. 150.000 ÷ 6.500 = **23,1 campañas** | OK |
| Vitalcan: 0,5% + 0,0275% + 0,5% | A8 E8003 | 1,0275% ≈ 1,03% | OK |
| a2censo: COP 111.300 M en USD | A2 l.142 | Con COP 3.900–4.400/USD da USD 25–28,5 M | OK (rango) |

**Observación sobre el 05:** en `Modelo_M1!B18:D18` (costo total para el emisor) hay una constante **+0.02** ("2% colocación del operador") escrita dentro de la fórmula y no en `Supuestos`. Es un supuesto oculto que debería pasar a la hoja `Supuestos`. Además, la nota de `Supuestos` fila `ticket` dice "sujeto del tope a confirmar": ya está confirmado que es por inversor (E9005). A9 no modificó el xlsx.

---

## 7. Revisión de `01_MAPA_COMPETITIVO.csv`

- **Formato:** el encabezado es exacto (15 columnas). Las 18 filas tienen 15 campos y no hay celdas vacías (los desconocidos dicen "No verificable"). ✔
- **`registro_verificado = Si`** aparece en 7 filas: Metro Futuro, Volsmart, Efaysto, Ripio, BYMA DA, Primary X y MAV. **Las 7 tienen respaldo oficial** (listado PSAV re-descargado por A9, E9010; MAV en el registro de mercados CNV, E1032). ✔
- **Correcciones de formato aplicadas por A9** (solo trazabilidad de la columna `fuente`):
  - Se reemplazó el texto "listado PSAV CNV" por la URL oficial (Efaysto, TokenByU, Allaria, Primary X).
  - Se agregó la URL del listado CNV donde había "Si: PSAV" sin fuente oficial en la columna (Ripio, Volsmart, BYMA DA).
  - Hay copia previa en el scratchpad de la sesión.
- **Observaciones de contenido que se devuelven a A1 (no se modificaron):**
  - `tokenizada_si_no` mezcla el valor con comentarios ("si (declarado, logo Polygon)"). Conviene dejar solo si/no y pasar el detalle a otra columna.
  - Fila Volsmart: "USD 4.150.330 recaudados" está en disputa (§5.7).
  - Fila Crowdium: "Fiduciario CFA inscripto…" es una declaración de Crowdium, no algo verificado.
  - Fila Landtoken: "Agro: campos operados por Adecoagro según prensa" no tiene ID de evidencia.

---

## 8. Lenguaje a corregir (archivo:línea → sugerencia)

| Ubicación | Texto | Problema | Sugerencia |
|---|---|---|---|
| frentes/A1_mercado_local.md:13 | "con emisión regulada" | "regulada" a secas | "con oferta pública autorizada por CNV según fuentes secundarias (E1016)" |
| frentes/A1_mercado_local.md:57 | "emisiones reguladas" | ídem | "emisiones con oferta pública CNV (pendiente AIF)" |
| frentes/A1_mercado_local.md:85 | "El único tokenizador local con emisiones bajo sandbox" | "único" falso (§5.9) | "uno de al menos dos (Volsmart y Tech Demeter/Justoken)" |
| frentes/A1_mercado_local.md:100 | "~20 proyectos fondeados" | Son 18 (E1006) | "18 proyectos" |
| frentes/A1_mercado_local.md:103 | "~ARS 16,8 billones … [S]" | Cifra sin ID | Agregar E1033 (pendiente: PDF no leído) |
| frentes/A8_red_team.md:14 | "[H/D] … USD 10.212 y 10.480 millones" | Mezcla una cifra oficial con una secundaria | "USD 10.480 M (CNV, E5024/E9013) [H]" |
| frentes/A8_red_team.md:15 y :95 | "no se encontró ningún caso … monto tokenizado colocado" / "no hay monto tokenizado colocado público" | Generalización contradicha (§5.8) | Ver la redacción de §5.8 |
| frentes/A8_red_team.md:42 y :45 | "El crowdfunding regulado lleva 9 años con uso marginal" | "regulado" a secas y conclusión sin dato (inferencia por ausencia, E8043) | "El régimen PFC (Ley 27.349) no tiene estadística pública de uso; fuentes secundarias sugieren uso marginal [I]" |
| frentes/A8_red_team.md:74 | "Contraejemplos [H]" que incluye MB/CVM "sin verificar por un 403" | Etiqueta incorrecta | Marcar la cita de E8037 como [S, no verificable] |
| frentes/A8_red_team.md:88 y :136 | "USD 94 M según Outlier" | Atribución errónea (E9016) | Quitar o buscar la fuente real |
| frentes/A5_insumos_economicos.md:13 y tabla l.53 | "no dice con claridad si esos topes rigen por inversor o por emisión" | Ya resuelto | "Topes por inversor (RG 1125 art. 148, E9005)" |
| frentes/A5_insumos_economicos.md:40 | "marketplace white label: Silver/Gold €18.000/año" | Error de lectura | "API Silver/Gold EUR 2.000/mes (18.000/año) + setup 2.000/7.000; Whitelabel desde EUR 2.500/mes" |
| frentes/A3_regulatorio.md:163 | "37 con las 5 actividades" | Error de conteo | "34 con las cinco actividades; 37 con cat. 5" |
| frentes/A7_tecnologia.md:36 | "la del primer FF tokenizado con oferta pública" | Superlativo de prensa | "presentado por la prensa como el primer…" (E5037) |
| frentes/A7_tecnologia.md:60 | "Las normas cambiaron 5 veces en 15 meses" | Período inexacto | "5 RG de tokenización/PSAV entre jun-2025 y oct-2026 (16 meses)" |
| 02_BENCHMARK_INTERNACIONAL.md:32 | Crowdcube "inversor 2,49%, emisor 7%" | Cifras sin URL ni ID | Agregar la fuente o quitarlas |
| 02_BENCHMARK_INTERNACIONAL.md:44 | "BBB y Trustpilot muestran quejas" | Sin URL | Agregar URL |
| 02_BENCHMARK_INTERNACIONAL.md:55 | "Kingscrowd … USD 7–8,6M por mes [S]" | Sin ID | Agregar ID/URL |
| 02_BENCHMARK_INTERNACIONAL.md:126 | "R$ 22M … según InvestNews" | Sin URL | Agregar URL |
| 02_BENCHMARK_INTERNACIONAL.md:173 | "~31%" | Denominador discutible | "31% de 154 (35% de las 137 que obtuvieron registro, E9018)" |
| 00_RESUMEN_EJECUTIVO.md:31, :50, :51 | Crowdium USD 13,8 M, UVA 1,5 M ≈ USD 2,1 M, UVA 3.000 ≈ USD 4.300 | Cifras sin ID | Agregar E1006, E3033/E9009 y E9005/E5043 |
| 10_DECISION.md:20, :25, :34 | "12,3 M de cuentas (A8)", Crowdium, topes | Sin ID | Agregar E8004, E1006 y E9005/E9009 |
| 04_MAPA_DE_PROCESOS.md:8, 06_MVP_Y_ARQUITECTURA.md:42, frentes/A7_tecnologia.md:25 | "regulado/s" | Uso genérico (aceptable) | Preferir "autorizado/registrado ante CNV como <figura>" |

**Búsqueda de términos prohibidos:**
- "lidera" y "mil usuarios": no aparecen.
- "garantizada": solo como nombre de instrumento ("ON PyME CNV Garantizada"). Es correcto.
- "líquido": solo aparece referido a productos rivales (caución), con respaldo E8031, o como término a bloquear (06:55). Es correcto.

---

## 9. Hallazgos devueltos a cada frente (lo que queda sin verificar)

**A1 — Mercado local**
- Corregir §5.9 (Justoken también es entidad generadora), el "~20 proyectos" y la redacción sobre Metro Futuro (§5.1).
- Sigue sin verificar:
  - RESFC-2026-23510 y RESFC-2026-23599 en la AIF.
  - Resultado de la licitación de Landtoken I y monto efectivamente tokenizado.
  - Monto de Illa Belgrano (E1014, contradictorio).
  - PDF del MAV/BCR (E1033).
  - Registro de PFC y ALyC (buscador por POST).
  - Direcciones de contratos on-chain (holders/supply).
  - Inscripción de CFA como fiduciario financiero.
- E1043 tiene `type=inferencia` pero agrupa varios enlaces rotos en una sola fila con URL de Volsmart. Conviene separarla.

**A2 — Benchmarks**
- Agregar URL o ID a Crowdcube, BBB/Trustpilot, Kingscrowd e InvestNews (§8).
- Pendientes:
  - Comisiones de Republic en fuente primaria (403).
  - E2016/E2017/E2019/E2020: todas salen de una sola reseña afiliada (angelinvestorsnetwork).
  - 8-K de Securitize (E2027/E2028).
  - Padrón CNBV de briq y Play Business.
  - FCA para Republic Europe.
  - Advertencias CNMV para Reental (E2052).
  - BrokerCheck.
- E2010 (lista FINRA) no fue re-verificable por A9 (403).

**A3 — Regulatorio**
- Corregir 37→34 (§4 del informe y E3040).
- Incorporar al 03 el efecto post-sandbox de RG 1150 art. 38: no habrá nuevas emisiones después del 31/12/2027 (E9006).
- Incluir el análisis de cat. 5 frente a Metro Futuro y plataformas similares como hipótesis para abogado (E9002).
- Pendientes:
  - Fecha de la RG 1172 en el B.O.
  - Texto de la Ley 27.739.
  - Vigencia de Res. UIF 49/2024 y 78/2023.
  - Registro de Agentes/PFC.
  - NT Tít. XI y Tít. VI Cap. IV.
  - Cita exacta del referenciamiento AN–PSAV en Tít. VII Cap. I.

**A5/A7 — Economía y tecnología**
- Actualizar el tope de la RG 1125 a "por inversor".
- Corregir la tabla de Brickken (E5007 fusionada en E2002).
- Sacar la constante +0.02 de `Modelo_M1` a `Supuestos`.
- Actualizar la nota `ticket` de `Supuestos`.
- Pendientes:
  - Anexo oficial RENAPER (E5020).
  - Form C de Republic leído completo (E5003).
  - Estado de ERC-1400 (E5034, github 403).
  - Tarifas de fiduciarias, ALyC y calificadoras para emisiones chicas.
  - Todo el bloque CAC/conversión/default, que es SUPUESTO sin ancla.
- La red usada por Landtoken I sigue sin dato.

**A8 — Red team**
- Corregir la atribución de USD 94 M a Outlier.
- Corregir la generalización "no hay monto tokenizado colocado" (§5.8).
- Citar CNV y no BCSF para el financiamiento pyme.
- Corregir la etiqueta [H] de la CVM/MB (E8037 es no verificable).
- Agregar fuente al 10-K de Overstock (E8020, SEC 403 al acceso automatizado) y reemplazar E8019 (410 Gone).
- Pendientes:
  - E8010 (cronología de RG por buscador).
  - E8023 (rwa.xyz).
  - E8029 (fecha de Induplack).
  - E8030 (BCRA Informe sobre Bancos).
  - E8042 (boletín BCR no leído).
  - E8041 (nota de 2019 usada como 2026: no usar).
- E8044/E8045 no tienen URL: son inferencias propias (se les asignó un URN).

**Todos los frentes (A1, A2, A5/A7, A8)**
- `accessed_at` con horas posteriores al reloj real de la sesión: 188 filas. Hay que registrar la hora real de acceso o aclarar que la hora es nominal.
- `published_at` con fechas parciales: 33 filas. Usar fecha completa o dejar vacío.

---

## 10. Veredicto de calidad

**Conclusiones robustas** (fuente oficial re-leída por A9, sin contradicciones):
- El registro PSAV no habilita oferta pública de VN (RG 1172 art. 38). El token no crea un VN nuevo ni derechos (Tít. XXII art. 7; Ley 26.831 art. 3).
- La definición de oferta pública es amplia y alcanza a medios electrónicos y redes (Ley 26.831 art. 2). El riesgo de que un portal con CTA sea promoción u oferta tiene base textual, aunque el encuadre concreto sigue siendo hipótesis para abogado.
- Topes: PFC UVA 1,5 M por proyecto. RG 1125: UVA 3.000 por emisión y 10.000 en total **por inversor**. Tokenización restringida a ≤5 PSAV con las cinco categorías (solo 34 PSAV las tienen hoy). El sandbox vence el 31/12/2027 y después **no se admiten nuevas emisiones** bajo ese régimen.
- Escala del mercado de capitales pyme no tokenizado: USD 10.480 M en 2025 (CNV).
- Los casos de fracaso internacionales (RealT, multas FINRA, cancelaciones CVM) son sólidos como contraejemplos.
- La economía del modelo es aritméticamente correcta: M2 base −12% y M1 base USD 6.500 por campaña. **Pero sus insumos son supuestos.**

**Conclusiones frágiles** (fuente secundaria, inferencia por ausencia o supuesto):
- **Tamaño y actividad de la oferta tokenizada local:** las 3 emisiones con oferta pública salen de notas de estudios jurídicos y prensa. No hay cotejo en la AIF. El monto efectivamente tokenizado se desconoce, y los montos de Illa Belgrano están en disputa.
- **Uso histórico del régimen PFC** ("marginal"): es una inferencia por ausencia. El registro de PFC nunca se consultó.
- **Costos de estructuración de emisiones chicas:** no hay ninguna cotización. La única referencia es un FF grande de consumo (2,18%) y una ON grande garantizada (1,03%).
- **CAC, conversión, recurrencia y default:** son SUPUESTOS sin ancla. El veredicto NO-GO de M2 y el PILOTO de M1 dependen de ellos.
- **Encuadre de M1** (fee de originación pagado a un no registrado, referenciador frente a AP/AAGI): hipótesis para abogado, como dice el propio 03.
- **Cifras de plataformas** (Crowdium USD 13,8 M, Raíz, Justoken, Reental, Brickken TTV): son declaraciones comerciales, varias con inconsistencias internas.
- **Comisiones de Republic y métricas de Reg CF:** dependen de una sola reseña afiliada.

**Qué cambiaría las conclusiones:**
- Cotejo en la AIF de los 3 FF tokenizados, con montos.
- Consulta manual del registro de agentes, PFC y fiduciarios de la CNV.
- 3 cotizaciones de estructuración (K3).
- Dictamen legal sobre el fee de originación (K4).

---

## 11. Limitaciones de A9

- No se consultaron registros CNV por formulario POST (PFC, ALyC, fiduciarios), por protocolo.
- No se leyó la AIF.
- Sitios con 403 (FINRA, SEC, The Block, BridgeDetroit, CriptoNoticias y otros): A9 no re-verificó su contenido salvo FINRA, vía fuente alternativa.
- El B.O. no permitió confirmar la publicación de la RG 1172.
- La re-verificación es por muestreo (24 de 253 filas). El resto conserva el estado que le asignó cada frente, salvo los ajustes listados en §2.
