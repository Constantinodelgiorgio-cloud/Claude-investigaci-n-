# A1 — Mercado local: actores, ofertas y evidencia (Argentina)

**Fecha de ejecución:** 2026-10-19 · **Frente:** A1 · **Insumos:** `research/01_MAPA_COMPETITIVO.csv` (18 filas), `research/frentes/A1_evidencia.csv` (E1001–E1043).
**Método:** lectura de sitios oficiales (WebFetch/curl), prensa y notas de estudios jurídicos (WebSearch), y **descarga del registro PSAV oficial de la CNV** (`/SitioWeb/Reportes/ListadoRegistrosPsav`, xlsx generado el 19/10/2026 a las 04:35, 80 personas jurídicas). No se crearon cuentas ni se enviaron formularios con datos personales. El único POST que se hizo fue una consulta al buscador público de agentes de la CNV, que no devolvió resultados (ver §6).

> Convención: **[V]** = verificado en fuente primaria u oficial · **[D]** = declarado por la empresa · **[S]** = fuente secundaria (prensa o estudio jurídico), pendiente de verificar en la Autopista de Información Financiera (AIF) · **[I]** = inferencia de A1.

---

## 1. Respuesta corta

- Sí hay **≥12 organizaciones** argentinas o con operación en Argentina vinculadas al tema: el mapa tiene 18. Pero **las que son realmente comparables** con un "marketplace de proyectos productivos tokenizados" con ofertas visibles para el público son **unas 6**: Metro Futuro, Raíz, Efaysto, Crowdium (sin token), Volsmart/Quality Home y Landtoken. El resto son infraestructura, distribución o sitios sin ofertas verificables.
- **Casi todo es inmobiliario.** Lo único productivo no inmobiliario con oferta pública autorizada por CNV según fuentes secundarias (E1016) es **agro/tierra (Landtoken I)**. No se encontró **ninguna ON pyme tokenizada ni ninguna emisión bajo la RG 1125 (crowdfunding automático)** al 19/10/2026 [S/I, E1038].
- Hay **tres emisiones tokenizadas con oferta pública CNV identificadas** (todas fideicomisos financieros): Landtoken I (campos), Illa Belgrano I (residencial CABA) y Espacio Añelo (vivienda para petroleras). Las tres vienen de notas de estudios jurídicos que citan resoluciones CNV [S]. Hay que cotejarlas en la AIF.
- El grueso del volumen "tokenizado" minorista corre **por fuera de la oferta pública**: fideicomisos privados o contratos, con o sin token. El inscripto ante la CNV, cuando existe, lo está **como PSAV**, y eso no habilita oferta pública. Metro Futuro y Efaysto lo dicen expresamente en sus sitios [V].

---

## 2. Clasificación de actores

| Categoría | Actores | ¿Opera ofertas para el público? |
|---|---|---|
| Emisor propio / marketplace tokenizado inmobiliario | Metro Futuro, Raíz Finance, Efaysto, TokenByU/BuildingTok | Metro Futuro y Raíz sí (declarado). Efaysto: 1 proyecto nombrado. TokenByU: "preventa" sin detalle |
| Crowdfunding no tokenizado | Crowdium (fideicomisos privados); ProBolsa PFC (no verificada) | Crowdium sí, con el historial más largo |
| Tokenizadora / estructuradora | Trustoken, BrickFlow, Volsmart (PSAV), Pala Blockchain | Trustoken y BrickFlow: **no se ven ofertas reales**. Volsmart: sí, vía FF con oferta pública |
| Emisor de activo productivo vía FF tokenizado | Landtoken (campos) | Sí (Landtoken I, dic-2025) |
| Distribución financiera | Allaria (ALyC + fiduciaria + PSAV), Ripio (PSAV), Banco Coinag (con Pala), MAV (cheques/pagarés pyme) | Sí |
| Infraestructura | Justoken (ex Agrotoken), BYMA Digital Assets, Primary X (Grupo A3), CFA (fiduciario) | B2B |

Quedan **fuera del mapa** por no ser proyectos productivos, aunque sí son RWA con presencia en Argentina: WIN Investments (futbolistas) y Slice Token (deportistas) [E1042]. La comparación con actores internacionales (Reental, Brickken, etc.) le corresponde a A2.

---

## 3. Conteo de ofertas verificables por estado y categoría

### 3.1 Ofertas listadas en sitios propios (declaradas por la empresa, consultadas el 19/10/2026)

| Plataforma | Activas / en financiación | Cerradas / agotadas / fondeadas | Finalizadas (salida) | Anunciadas | Categoría | ¿Token? |
|---|---|---|---|---|---|---|
| Crowdium | 2 | 18 (suma declarada USD 13,8 M) | 3 (sin retorno realizado publicado) | — | Inmobiliario (incluye 1 en NY) | No |
| Metro Futuro | 3 | 4 ("agotado", sin montos) | 0 | 2 | Inmobiliario: AR 5, ES 3, UY 1 | Sí |
| Raíz Finance | 1 | 3 ("sold out") | 0 | — | Inmobiliario AR/EE.UU. | Sí |
| Efaysto | No verificable (1 proyecto nombrado) | — | — | — | Inmobiliario de pozo | Sí |
| TokenByU/BuildingTok | "preventa" (2 productos) | — | — | — | Inmobiliario + oro | Sí |
| BrickFlow | 0 visibles | 0 | 0 | 0 | Inmobiliario | Sí (declarado) |
| Trustoken | 1 mostrada (probable maqueta) | — | — | — | Inmobiliario | Sí (declarado) |
| **Total (Crowdium + Metro Futuro + Raíz)** | **6** (incluye Next Bustamante II, de estado ambiguo) | **25** | **3** | **2** | ~100% inmobiliario | |

### 3.2 Emisiones con oferta pública CNV y representación digital [S, pendientes de AIF]

| Emisión | Activo | Resolución citada | Monto | Partes | Estado |
|---|---|---|---|---|---|
| FF Inmobiliario Landtoken I | Campos agrícolas | Oferta pública (nro. no citado), colocación 9–16/12/2025 | VN USD 4.777.518 primer tramo (USD 2.192.500 en especie por los campos aportados), oferta hasta USD 20 M | Allaria Fiduciaria, Allaria S.A. + 6 subcolocadores, Justoken, Landtken S.A. | Colocada. Token LAND en Ripio desde 06/04/2026 |
| FF Illa Belgrano I | Residencial CABA (pozo) | RESFC-2026-23510 (08/04/2026) | USD 4.150.330 según Lexlatin (sin documento primario) | CFA, Arg Capital, Coruba, Volsmart | Autorizada. Estado actual no verificable |
| FF Espacio Añelo | 20 UF alquiladas a petroleras | RESFC-2026-23599 (22/07/2026) | No informado | CFA, ARG Capital, Idero, Volsmart | Autorizada. Estado no verificable |

**Por categoría (emisiones con oferta pública CNV, pendiente de cotejo en AIF):** inmobiliario urbano 2 · agro/tierra 1 · pyme industrial/servicios **0** · energía **0** (Justoken menciona un activo de YPF Luz por USD 800 M, que es declaración comercial y no tiene oferta minorista identificada).

### 3.3 Transacciones con evidencia
- Hay documentación de terceros con montos para **Landtoken I** (estudio jurídico) y, con menos solidez, para **Illa Belgrano** (Lexlatin).
- **Crowdium** publica montos por proyecto en su propio sitio. Es la única serie histórica larga, pero **no está auditada** y no tiene token.
- **Metro Futuro, Raíz, Justoken, Pala, Trustoken y BrickFlow:** solo cifras de marketing, o ninguna. Los contadores de la home de Metro Futuro están en 0. Raíz da cifras inconsistentes dentro de su propio sitio (25.000 vs 27.000 usuarios, USD 2 M vs 2,5 M).
- No se intentó verificar en blockchain (contratos/holders), porque ningún sitio publica direcciones de contrato de forma accesible. **Pendiente:** pedir direcciones de contrato y contrastar cantidad de holders y supply.

---

## 4. Quién opera de verdad y quién solo promociona tecnología

**Operan con ofertas visibles:** Crowdium (desde hace años, sin token), Metro Futuro, Raíz, Landtoken + Allaria + Ripio, Volsmart/Quality Home.
**Infraestructura con uso documentado:** Justoken (generó los CP digitales de Landtoken I), BYMA Digital Assets (servicio de registro lanzado), CFA (fiduciario de los fideicomisos de Crowdium y de dos FF tokenizados), MAV (financiamiento pyme no tokenizado, a escala).
**Solo promocionan tecnología o no tienen ofertas comprobables:**
- **Trustoken:** su única "ronda activa" aparece junto a un dominio placeholder. Lo más probable es que sea una maqueta.
- **BrickFlow:** sin proyectos, sin entidad legal, con los enlaces legales rotos.
- **Pala:** anuncia +20 desarrolladores y alianzas con Bitget y Coinag, pero no publica ningún proyecto nombrado.
- **TokenByU/BuildingTok:** versión 0.1.0, "preventa", y el CUIT del sitio **no coincide** con el registro CNV. Es una señal de alerta (E1026, *contradictorio*).
- **Efaysto:** es PSAV desde el 16/09/2026, pero tiene un solo proyecto sin datos.

---

## 5. Relación con la CNV (lo verificado contra lo declarado)

| Actor | Vínculo CNV verificado | Observación |
|---|---|---|
| Metro Futuro SRL | PSAV N° 100 [V] | Solo intercambio y transferencia. **No** tiene registradas custodia ni "participación en oferta de emisor". Vende tokens propios igual |
| VOL PRO SRL (Volsmart) | PSAV N° 85 [V] + FF autorizados [S] | Uno de al menos dos generadores locales de representaciones digitales con emisiones CNV identificadas (2); el otro es Tech Demeter/Justoken en Landtoken I (corrección A9 §5.9) |
| Real World Assets S.A. (Efaysto) | PSAV N° 172 [V] | Alta muy reciente |
| Building TOC S.A. (Token ByU) | PSAV N° 173 [V] | El sitio declara otra razón social y otro CUIT → **contradictorio** |
| Allaria Digital / Moonbird (Ripio) / Caja Digital Assets (BYMA) / BTGT (Bitget) / Primary X | PSAV N° 132 / 36 / 86 / 168 / 170 [V] | Distribución e infraestructura |
| MAV | Mercado, matrícula 15 [V] | Financiamiento pyme no tokenizado |
| Crowdium / CFA | CFA, fiduciario financiero (declarado) | Crowdium aclara que sus fideicomisos **no** son oferta pública |
| Trustoken, BrickFlow, Raíz, Pala, Justoken | No figuran como PSAV [V: ausencia en el listado] | Raíz muestra el logo de la CNV sin indicar ningún registro |
| PFC (cualquiera) | **No verificable** | El buscador de agentes no respondió. ProBolsa PFC aparece citada solo por una fuente secundaria |

**Hallazgo clave:** en el mercado minorista tokenizado, el registro PSAV se usa como **señal de confianza comercial**, aunque las propias empresas aclaran que no implica supervisión de la actividad. A3 debe evaluar si vender tokens con derechos económicos sobre un vehículo inmobiliario, sin oferta pública, encuadra como valor negociable. Crowdium sostiene que sus productos "no son valores negociables" [V]. Es una **hipótesis para abogado**.

---

## 6. Señales: qué problema existe y quién paga

1. **Hay oferta de desarrolladores inmobiliarios que buscan fondeo minorista en USD.** Crowdium muestra 18 proyectos fondeados (E1006) de USD 0,3–2,5 M cada uno (promedio declarado ~USD 0,77 M). Es la mejor evidencia local de que existe demanda minorista por ticket bajo y de que **el desarrollador paga**: margen o fee de estructuración y administración. **Para eso no hizo falta token.**
2. **El token aparece como canal de distribución, no como necesidad del activo.** Landtoken I se colocó a la vez por siete ALyC y por un exchange (Ripio). Lo tokenizado amplía el alcance, pero la emisión es un FF clásico con fiduciario y ALyC. **Quien paga** es el emisor/organizador (fees de fiduciario, colocación, tokenización y PSAV). Según prensa de 2024, Landtoken cobraba al inversor 2–3,5% de entrada, 5% de la renta y 0,75% a la salida [S, baja].
3. **La liquidez prometida no se demuestra.** Raíz promete salir en 48 h, pero su disclaimer dice que "no existe un mercado público" para sus tokens. Metro Futuro ofrece P2P "sujeto a demanda". **No hay evidencia de mercado secundario profundo.**
4. **Las pymes no inmobiliarias ya tienen un canal masivo sin token.** El MAV negoció ~ARS 16,8 billones en cheques, pagarés y FCE en el primer semestre de 2026 [S]. Un marketplace de "proyectos productivos" compite con ese canal en costo y velocidad.
5. **El régimen PFC casi no se usó desde 2017** [S], y la RG 1125 (abril 2026) todavía no muestra emisiones públicas identificables. El problema regulatorio en sí parece estar resuelto. **El cuello de botella está en la originación y la distribución.** Esto es una inferencia y hay que validarlo con A4.

## 7. Huecos de mercado (hipótesis, no validadas)

- **Proyectos productivos no inmobiliarios** (agro distinto de la tierra, energía distribuida, maquinaria, ganadería): no hay ofertas minoristas con oferta pública fuera de Landtoken.
- **Agregador o comparador neutral** de ofertas inmobiliarias fraccionadas (Crowdium, Metro Futuro, Raíz, FF tokenizados) con información estandarizada: estructura jurídica, fiduciario, registro, historial de pagos. Hoy cada plataforma publica en su propio formato y sin datos de cumplimiento ex post (retornos efectivamente pagados).
- **Due diligence y reporting estandarizado** de proyectos para ALyC y PSAV (B2B). Los colocadores ya existen; falta originación filtrada.
- **ON pyme tokenizadas bajo RG 1125:** el marco existe y no se identificaron emisiones. Es una oportunidad, pero también puede ser señal de falta de demanda o de costo de estructuración. Lo debe contrastar A8.

## 8. Enlaces rotos o no concluyentes

| URL | Resultado |
|---|---|
| http://volsmart.com.ar/ (sitio declarado en el registro CNV) | DNS no resuelve. Se usó https://www.volsmart.com/ (SPA sin texto) |
| https://crowdium.ar/proyectos | 404. La ruta válida es /proyectos-de-inversion |
| https://www.brickflow.com.ar/proyectos | Renderiza "Cargando..." sin datos. Links legales "#" |
| https://www.landtoken.com | Redirige a un vendedor de dominios. landtoken.com.ar no responde. Sitio oficial no ubicado |
| https://pala.la, https://www.palablockchain.com | Sin respuesta. Sitio oficial no ubicado |
| https://probolsa.com.ar | Solo título, sin contenido |
| https://agrotoken.com | 301 a justoken.com (cambio de marca o absorción) |
| https://www.efaysto.ar | 301 a efaysto.com |
| Buscador CNV de agentes (POST /RegistrosPublicos/BusquedaAgentes y BusquedaPsav) | Tabla vacía en consultas automatizadas, incluso con nombres conocidos. **Hace falta una consulta manual humana para PFC y ALyC** |

## 9. Limitaciones y pendientes para el orquestador, A3 y A9

1. Verificar en la **AIF/CNV** las resoluciones RESFC-2026-23510 y RESFC-2026-23599, el resultado de colocación de Landtoken I y las ofertas o hechos relevantes posteriores.
2. **Consulta manual** del registro de agentes CNV, categoría "PLAT. FINAN. COLECT.", para contar PFC activas; y verificación de la matrícula ALyC de Allaria.
3. Pedir y contrastar en blockchain las direcciones de contrato de Metro Futuro, Raíz y LAND (holders, supply).
4. A3: encuadre de los tokens inmobiliarios sin oferta pública (Metro Futuro, Raíz, Efaysto, TokenByU) y alcance de las actividades PSAV registradas por Metro Futuro, que no incluyen "participación en oferta de emisor".
5. A9: auditar la discrepancia de CUIT de TokenByU (E1025 vs E1026) y la inconsistencia de cifras de Raíz.
6. Las cifras de usuarios e inversores (Crowdium 153.877, Raíz 25–27 mil, Justoken USD 2.840 M) son **declaraciones comerciales** y no deben usarse como tamaño de mercado.
