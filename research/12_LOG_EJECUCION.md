# 12 — Log de ejecución

**Fecha de ejecución:** 2026-10-19 (alrededor de 07:25–08:10 UTC) · **Entorno:** sesión de Claude Code en la nube con orquestador y subagentes en paralelo, en modo `/loop` autorregulado · **Repositorio:** rama `claude/rwa-argentina-research`.

## 1. Agentes ejecutados

| Frente | Ejecución | Salidas | Evidencia |
|---|---|---|---|
| Orquestador | Sesión principal | `00`, `04`, `05` (xlsx + csv), `06`, `07`, `10`, `12`; protocolo común; integración de correcciones de A9 | — |
| A1 Mercado local | Subagente en paralelo | `01_MAPA_COMPETITIVO.csv` (18 filas), `frentes/A1_mercado_local.md` | E1001–E1043 |
| A2 Benchmarks internacionales | Subagente en paralelo | `02_BENCHMARK_INTERNACIONAL.md` (15 modelos), `frentes/A2_internacionales.csv` | E2001–E2052 |
| A3 Jurídico/regulatorio | Subagente en paralelo | `03_DICTAMEN_REGULATORIO_PRELIMINAR.md`, `11_PREGUNTAS…` (27 preguntas), `frentes/A3_regulatorio.md`, anexo del registro PSAV | E3001–E3050 |
| A4 Descubrimiento de clientes | Orquestador (sin subagente: no requería fuentes web) | `07_PLAN_DE_VALIDACION.md` | — |
| A5/A7 Insumos económicos y tecnología | Subagente en paralelo | `frentes/A5_insumos_economicos.md`, `frentes/A7_tecnologia.md` | E5001–E5043 |
| A6 Producto/procesos | Orquestador | `04_MAPA_DE_PROCESOS.md` (journeys, BPMN conceptual, RACI) | — |
| A8 Red team | Subagente en paralelo | `frentes/A8_red_team.md`, `08_RIESGOS_Y_KILL_CRITERIA.md` (15 riesgos, 14 kill criteria) | E8001–E8046 |
| A9 Auditor / QA | Subagente posterior (fase III) | `frentes/A9_auditoria.md`, `09_EVIDENCIAS.csv` (253 filas, 0 errores de schema), `tools/validar_evidencia.py` | E9001–E9024 |

## 2. Tareas completadas

Están los 13 entregables del mandato §5. El modelo económico tiene fórmulas editables en `.xlsx` (`tools/build_model.py` lo regenera) y un `.csv` espejo con los valores.

A9 releyó 24 afirmaciones críticas en la fuente: las 9 regulatorias del dictamen se confirmaron.

Correcciones de A9 incorporadas por el orquestador:
- topes de la RG 1125 por inversor;
- efecto del vencimiento del sandbox, agregado en `03` y `08`;
- conteo PSAV: 34 con las cinco actividades;
- atribución de RealT a Outlier;
- precios de Brickken;
- tasa de cancelación CVM;
- contradicciones Landtoken / "único tokenizador";
- "regulado" a secas;
- IDs de evidencia en `00` y `10`;
- constante oculta del 2% en `Modelo_M1`, que pasó a `Supuestos`.

## 3. Tareas incompletas y bloqueos

| Pendiente | Motivo | Quién / cómo |
|---|---|---|
| Consulta del registro de Agentes CNV (PFC, ALyC, AP, AAGI, ACVN) | El buscador exige enviar un formulario y el protocolo prohíbe enviarlos; además devolvió tablas vacías a consultas automatizadas | Humano, consulta manual por CUIT |
| Cotejo en la AIF de las RESFC-2026-23510 y 23599 y del resultado de colocación de Landtoken I | No se leyeron los documentos en la AIF | Humano o una nueva corrida |
| Prospecto de Landtoken I (red usada, monto tokenizado) | No se leyó | Nueva corrida |
| Cotizaciones de estructuración, colocación, fiduciario y abogados | Requiere contactar terceros (prohibido) | Humano (K3) |
| Entrevistas (18) y LOI | Requiere contactar terceros; **no se simuló ninguna** | Humano (`07`) |
| Ley 27.739 en texto propio; Código Penal (intermediación no autorizada); NT Tít. XI, Tít. VI Cap. IV y Tít. XIV Cap. II; BCRA (PSP); impuestos | Sin leer (no localizada o fuera del tiempo disponible) | Abogado (`11`) |
| Modificaciones posteriores de las Res. UIF 49/2024 y 78/2023 | Sin verificar | Abogado |
| Contradicciones abiertas: monto de Illa Belgrano; CUIT de Token ByU; inscripción de CFA como fiduciario | Fuentes insuficientes | Ver `frentes/A9_auditoria.md` §5 |
| Ajustes menores de redacción que A9 sugirió en `02` (cifras de Crowdcube, Kingscrowd, InvestNews y BBB sin URL) | No se corrigieron | Pendiente (frente A2) |

## 4. Advertencias

- **Costos:** 6 subagentes, entre unos 160 mil y 330 mil tokens cada uno, más el orquestador. No se contrató ni gastó dinero en servicios.
- **Marcas de tiempo:** 188 filas de evidencia tienen un `accessed_at` nominal (hora estimada por el agente, no medida); la fecha 2026-10-19 sí es correcta (A9 §2).
- **Calidad:**
  - Son robustas las barreras regulatorias, que el token no aporte derechos ni liquidez, y los contraejemplos internacionales.
  - Son frágiles el tamaño de la oferta tokenizada local, el uso histórico de las PFC, los costos de estructuración, los supuestos de CAC y conversión, y el encuadre legal de M1 (A9 §10).
  - **El NO-GO de M2 y el piloto de M1 dependen de supuestos sin validar.**

## 5. Enlaces rotos o bloqueados

De 178 URL únicas:
- 152 respondieron 200;
- 22 dieron 403 (anti-bot: Republic, Wefunder, Crowdcube, FINRA, entre otros);
- 1 dio 410 (Cointelegraph, E8019);
- 1 dio 429;
- 2 fallaron de forma transitoria.

Además:
- QR Tokenizadora dio 502.
- No resolvieron volsmart.com.ar, landtoken.com, pala.la, crowdium.ar/proyectos ni probolsa.com.ar.
- Varios avisos del Boletín Oficial devolvieron 503 o un reset de forma intermitente.

Detalle en `frentes/A9_auditoria.md` §4 y en el informe de cada frente.

## 6. Próximos pasos

Están en `00_RESUMEN_EJECUTIVO.md` §"3 siguientes acciones" y `10_DECISION.md`:
1. Contratar un abogado y obtener el dictamen sobre los escenarios 1, 2 y 8 antes del 2026-11-18.
2. Hacer las entrevistas y conseguir las LOI antes del 2026-12-18 (K1, K2).
3. Conseguir las cotizaciones y decidir en el día 90, el 2027-01-17.

No construir software financiero antes de esa fecha.
