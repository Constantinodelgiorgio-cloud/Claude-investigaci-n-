# A5 — Insumos para el modelo económico (unit economics)

**Frente:** A5 (insumos) · **Fecha de ejecución:** 2026-10-19 (Argentina) · **Evidencia:** `A5A7_evidencia.csv` (IDs E5001–E5043)
**Conversión usada (solo para orientación):** UVA = ARS 2.159,10 al 19/10/2026 (BCRA, API Estadísticas v4.0, variable 31, E5043); USD mayorista de referencia = ARS 1.514,57 al 16/10/2026 (BCRA, variable 5). Las equivalencias en USD son **inferencias** y no datos de la fuente original.

> Regla de este documento: **DATO** = valor tomado de una fuente con URL, consultada en esta fecha. **SUPUESTO** = valor que propone este frente para modelar, sin respaldo externo suficiente. Ningún SUPUESTO puede presentarse como dato en el modelo `05_MODELOS_DE_NEGOCIO`.

---

## 1. Hallazgos que cambian el modelo (leer primero)

1. **Los topes regulatorios del crowdfunding argentino limitan el GMV posible por proyecto.** En el régimen PFC vigente (Normas CNV, Título XIV, Cap. I, texto actualizado), un proyecto puede emitir como máximo **UVA 1.500.000 en 12 meses** (≈ ARS 3.239 M ≈ USD 2,1 M), cada inversor puede poner como máximo **el menor entre 10% del proyecto y UVA 150.000** (un inversor calificado, hasta el 20%), hace falta un **mínimo de 5 inversores** y nadie puede destinar a crowdfunding más del **20% de sus ingresos brutos anuales**. [E5009, E5010]
2. **El nuevo régimen de crowdfunding con autorización automática (RG CNV 1125/2026, abril 2026) es todavía más chico para el minorista.** Según el comunicado oficial, los topes son de **UVA 3.000 por emisión y UVA 10.000 en total** (≈ USD 4.300 y ≈ USD 14.300), con límites de 5% del patrimonio por proyecto y 10% del total invertido. **Inferencia (para que A3 la confirme con el texto de la RG):** el comunicado no dice con claridad si esos topes rigen por inversor o por emisión. Si fueran por emisión, el régimen sería apenas testimonial. [E5011] **[Corrección A9: los topes son por inversor — RG 1125 art. 148 NT 'LÍMITES POR INVERSOR', E9005.]**
3. **Los costos fijos de las estructuras reguladas pesan mucho en emisiones chicas.** En un fideicomiso financiero real de 2025 (FF Total Assets V, de VN ARS 18.836 M), los gastos sin impuestos estimados en el prospecto suman **≈2,18% del VN**: colocación 0,89%, fiduciario 0,44% y CNV/CVA/BYMA/MAE 0,16%. Si se agrega Ingresos Brutos, el total pasa a ≈12%, porque ese impuesto se calcula sobre los flujos. Es un FF de consumo grande. En una emisión pyme de USD 0,2–2 M, la parte fija de esos costos sube mucho como porcentaje. **No encontramos tarifas públicas de fiduciarias ni de estructuradores para emisiones chicas.** [E5016]
4. **El KYC dejó de ser una barrera de costo.** Hay precios públicos de entre **USD 0,80 y 1,89 por verificación** (Veriff, Sumsub) y validación RENAPER de **ARS 20–60 por transacción** (≈ USD 0,01–0,04). El costo de KYC es chico al lado del CAC y del costo legal por emisor. [E5018–E5022]
5. **Del CAC no hay benchmarks confiables con fuente primaria para LatAm.** Todo valor de CAC es **SUPUESTO**. Es la variable más incierta del modelo, junto con la conversión.
6. **Las comisiones internacionales de referencia se ubican entre 6% y 8% de lo captado, en efectivo, más alrededor de 2% en títulos, pagados por el emisor, y 2–3,5% pagados por el inversor.** Wefunder cobra 7,9% de éxito más una tarifa anual. En Republic los Form C muestran 6–7% más 2% en títulos. En StartEngine una circular Reg A muestra 3,5% más un warrant del 2% más una tarifa de 3,5% al inversor (tope USD 700). No hay que trasladar estas cifras a Argentina sin ajustar por los topes locales. [E5001–E5006]

---

## 2. Tabla de parámetros

Formato: `parámetro;valor;unidad;fuente;fecha;certeza` (la columna «clase» distingue DATO de SUPUESTO).

### 2.1 Comisiones de plataformas (DATO)

| clase | parámetro | valor | unidad | fuente | fecha | certeza |
|---|---|---|---|---|---|---|
| DATO | Wefunder: comisión al emisor (Reg CF, solo si tiene éxito) | 7,9 | % del monto captado | https://wefunder.helpjuice.com/getting-started-for-founders/303756-how-does-wefunder-make-money (E5001) | consultado 2026-10-19 | alta (doc. primario) |
| DATO | Wefunder: tarifa anual de administración posterior al cierre | menor entre USD 1.000 y 0,5% de lo captado | USD/año | ídem (E5001) | 2026-10-19 | alta |
| DATO | Wefunder: tarifa al inversor (ACH/wire) | 2 (mín. USD 8, máx. USD 150) | % por transacción | https://wefunder.helpjuice.com/investing/what-fees-does-wefunder-charge-investors (E5002) | 2026-10-19 | alta |
| DATO | Wefunder: tarifa al inversor (tarjeta/Apple Pay) | 5,5% + USD 2 | por transacción | ídem (E5002) | 2026-10-19 | alta |
| DATO | Republic (OpenDeal Portal LLC): comisión al emisor según Form C | 6–7% en efectivo + 2% en títulos; en 2026 aparece un esquema escalonado (0% hasta USD 100k, 6% sobre el excedente, mínimo USD 15k) + USD 7.500 de onboarding | % / USD | Form C en EDGAR, p. ej. https://www.sec.gov/Archives/edgar/data/1938967/000193896726000001/metainto.pdf (E5003) | 2026 (Form C) | media: varía por oferta, y la página oficial de tarifas dio 403 |
| DATO (secundario) | Republic: tarifa administrativa al inversor | 2,5% (mín. USD 5, máx. USD 250) | % | https://angelinvestorsnetwork.com/capital-raising/republic-review-2026-equity-crowdfunding-platform (E5004) | 2026 | baja (fuente secundaria afiliada) |
| DATO | StartEngine: comisión al emisor en oferta Reg A (Lift Aircraft) | 3,5% en efectivo + warrant por 2% + USD 15.000 de gastos anticipados | % / USD | https://www.sec.gov/Archives/edgar/data/1889418/000110465922106215/tm227970d4_253g2.htm (E5005) | 2022-10-04 | alta para esa oferta, media como tarifa general |
| DATO | StartEngine: tarifa de procesamiento al inversor | 3,5% (máx. USD 700) | % | ídem (E5005) | 2022-10-04 | alta para esa oferta |
| DATO | Reental: comisiones (lanzamiento / alquiler / venta) | 10 / 2 / 40 | % | https://www.elindependiente.com/economia/2022/11/20/el-blockchain-llega-a-la-inversion-inmobiliaria-reental-ofrece-rentabilidades-del-10/amp/ (E5006) | 2022-11-20 | baja (prensa de 2022, sin confirmar vigencia; la base de cálculo del 40% no está clara) |
| DATO | Brickken Issuer Studio (SaaS de tokenización) | Core €3.000/año (€299/mes), Advanced €5.000/año, Professional €9.000/año, Enterprise a medida | EUR | https://www.brickken.com/plans (E5007) | 2026-10-19 | alta (doc. primario) |
| DATO | Brickken: KYC incluidos por año / KYC adicional | 50 / 150 / 500 / 1.000 unidades; adicional €3,50 cada uno | unidades / EUR | ídem (E5007) | 2026-10-19 | alta |
| DATO | Brickken: activos extra; marketplace white label | €100–200 por mes por activo; API Silver/Gold EUR 2.000/mes (18.000/año) + setup 2.000/7.000; Whitelabel desde EUR 2.500/mes; Enterprise EUR 1.999/mes (corrección A9) | EUR | ídem (E5007) | 2026-10-19 | media |
| DATO | Crowdium (AR): comisión pública al inversor o al emisor | **No encontrada**. Solo consta que cada proyecto es un fideicomiso con fiduciaria registrada en CNV y que el registro es gratuito | — | https://www.ambito.com/negocios/crowdium/cumple-anos-y-regala-7-millones-pesos-sus-usuarios-n5567673 (E5008) | s/f | baja. Pendiente: leer contratos de adhesión |

### 2.2 Marco regulatorio argentino con impacto económico (DATO)

| clase | parámetro | valor | unidad | fuente | fecha | certeza |
|---|---|---|---|---|---|---|
| DATO | PFC: monto máximo por proyecto (12 meses, todos los instrumentos) | 1.500.000 (≈ ARS 3.239 M ≈ USD 2,14 M) | UVA | Normas CNV T.XIV Cap. I art. 45 (texto actualizado): https://www.argentina.gob.ar/normativa/recurso/219405/texact-TituloXIV-CapI/htm ; RG 942/2022 https://www.boletinoficial.gob.ar/detalleAviso/primera/276517/20221125 (E5009) | 2022-11-25 (vigente en el texto actualizado consultado) | alta |
| DATO | PFC: tope por inversor y proyecto | menor entre 10% del proyecto y UVA 150.000 (≈ USD 214k). Calificado: 20% | % / UVA | ídem, art. 56 (E5009) | ídem | alta |
| DATO | PFC: mínimo de inversores por proyecto | 5 | inversores | ídem, art. 56 (E5009) | ídem | alta |
| DATO | PFC: tope anual por inversor | 20% de los ingresos brutos anuales (DDJJ) | % | ídem, art. 55 (E5010) | ídem | alta |
| DATO | PFC: patrimonio neto mínimo | 65.350 (≈ ARS 141 M ≈ USD 93k) | UVA | ídem, art. 11 (E5010) | ídem | alta |
| DATO | PFC: sobresuscripción máxima | 25% del monto original | % | ídem, Cap. I (E5010) | ídem | alta |
| DATO | Crowdfunding con autorización automática (RG 1125/2026): topes | Por inversor (art. 148, E9005): UVA 3.000 por emisión y UVA 10.000 en total. Límites de 5% del patrimonio por proyecto y 10% del total | UVA / % | Comunicado oficial, 07/04/2026: https://www.argentina.gob.ar/noticias/la-cnv-habilita-el-crowdfunding-con-autorizacion-automatica-y-amplia-las-alternativas-de (E5011) | 2026-04-07 | media: es comunicado y no texto normativo, y el sujeto del tope es ambiguo. A3 debe confirmarlo |
| DATO | Régimen de mediano impacto (acciones/ON) | tope elevado de UVA 7 M a UVA 15 M | UVA | ídem (E5011) | 2026-04-07 | media (comunicado) |
| DATO | Arancel de autorización CNV: ON autónoma / FF (emisión) | 0,05 | % del monto autorizado | Res. ME 1/2026, Anexo II (IF-2026-01214695-APN-CNV#MEC), BO 07/01/2026: https://www.boletinoficial.gob.ar/detalleAviso/primera/337165/20260107?anexos=1 (E5012) | 2026-01-07 | alta |
| DATO | Arancel CNV: programa global (ON/FF) + colocación de serie | 0,01% del programa + 0,04% de lo colocado | % | ídem (E5012) | 2026-01-07 | alta |
| DATO | Arancel CNV: ON/FF SVS, ON impacto social y **FF destinados a financiamiento pyme** (emisión autónoma) | 0,015 | % del monto autorizado | ídem (E5012) | 2026-01-07 | alta |
| DATO | Tasa anual de fiscalización: emisoras de acciones/ON/VCP | ARS 2.805.000 (≈ USD 1.852) | ARS/año | ídem (E5013) | 2026-01-07 | alta |
| DATO | Tasa anual: fiduciario financiero | ARS 5.611.000 (≈ USD 3.705) | ARS/año | ídem (E5013) | 2026-01-07 | alta |
| DATO | Tasa anual: PSAV persona jurídica / humana | ARS 13.360.000 / 5.344.000 (≈ USD 8.821 / 3.528) | ARS/año | ídem (E5013) | 2026-01-07 | alta |
| DATO | Tasa anual: ALyC (integral o propio) / AN / Agente Productor / AAGI | 18.704.000 / 2.338.000 / 655.000 / 2.620.000 | ARS/año | ídem (E5013) | 2026-01-07 | alta |
| DATO | Tasa anual: PFC | **No figura en el Anexo II de la Res. ME 1/2026** (no hay renglón «Plataforma de Financiamiento Colectivo») | — | ídem (E5014) | 2026-01-07 | media: puede estar alcanzada por otra categoría. Pregunta para abogado |
| DATO | Examen de idoneidad CNV (total / parcial) | ARS 103.000 / 65.000 | ARS | Anexo I, ídem (E5015) | 2026-01-07 | alta |
| DATO | Vigencia del sandbox de tokenización CNV | hasta 31/12/2027 (RG 1150/2026) | fecha | https://www.argentina.gob.ar/noticias/ampliacion-del-regimen-de-tokenizacion-valores-negociables-con-oferta-publica-automatica-y (E5032) | 2026-06-10 | alta |

### 2.3 Costos de estructuración (DATO puntual + vacío)

| clase | parámetro | valor | unidad | fuente | fecha | certeza |
|---|---|---|---|---|---|---|
| DATO | FF Total Assets V: gastos sin impuestos sobre VN (VN ARS 18.835.864.000) | ≈2,18% (ARS 411,2 M): colocación 0,89%, fiduciario 0,44%, administrador 0,38%, auditoría 0,14%, asesor impositivo 0,16%, CNV/CVA/BYMA/MAE 0,16%, otros 0,02% | % del VN | Adenda al Suplemento de Prospecto, TMF Trust / BST: https://www.bst.com.ar/wp-content/uploads/2025/04/FF-Total-Assets-V-Adenda-Suplemento-de-Prospecto-1.pdf (E5016) | 2025-04 | alta para ese FF. **Baja como referencia pyme**: FF de consumo grande, con honorarios que se reparten a lo largo de la vida del fideicomiso |
| DATO | Ídem, incluidos IIBB e IVA | ARS 2.272 M (≈12% del VN) | ARS | ídem (E5016) | 2025-04 | alta (dato del prospecto). IIBB domina |
| DATO | Honorario de administración del fiduciario en un FF público (FoGAr) | 1% anual sobre el activo administrado | %/año | https://www.boletinoficial.gob.ar/detalleAviso/primera/244095/20210508 (E5017) | 2021-05-08 | baja como benchmark privado |
| DATO | Tarifa pública de fiduciarias, estructuradores, ALyC colocadores o calificadoras para FF/ON pyme | **No hay fuente pública**. Se negocia caso a caso | — | búsqueda sin resultados (ver §5) | — | — |
| DATO | ON Pyme CNV Garantizada: costos típicos | **No hay fuente pública con tarifas vigentes**. El comunicado de la CNV (jul-2026) anuncia una ON simplificada pyme con mínimo de ARS 500.000 y aval SGR | — | https://www.sitioandino.com.ar/n/227978-la-comision-nacional-de-valores-lanzara-nuevas-herramientas-para-pymes (E5026) | 2026-07-21 | baja (prensa) |

### 2.4 KYC, identidad y firma (DATO)

| clase | parámetro | valor | unidad | fuente | fecha | certeza |
|---|---|---|---|---|---|---|
| DATO | Sumsub Basic / Compliance (incluye AML) | USD 1,35 / 1,85 por verificación; mínimos de USD 149 / 299 por mes | USD | https://sumsub.com/pricing/ (E5018) | 2026-10-19 | alta |
| DATO | Veriff Essential / Plus / Premium | USD 0,80 / 1,39 / 1,89 por verificación; mínimos de USD 49 / 99 / 209 por mes | USD | https://www.veriff.com/pricing (E5019) | 2026-10-19 | alta. TrustRadius publica otros valores (contradictorio, desactualizado) |
| DATO | RENAPER: validación de DNI vía API REST (convenio), por volumen mensual | ARS 60 (hasta 40.000), 35 (40.001–2 M), 20 (>2 M) por transacción | ARS | Res. MI 19/2026 (BO 03/03/2026), resumida en https://www.derechoenzapatillas.com/2026/nuevas-tasas-renaper-registro-nacional-de-las-personas/ (E5020) | 2026-03-03 | media: fuente secundaria. Verificar el anexo IF-2026-20279196-APN-RENAPER#MI |
| DATO | RENAPER: prueba de vida pasiva / verificación de pasaporte | ARS 70 c/u | ARS | ídem (E5020) | 2026-03-03 | baja (la tabla secundaria está desordenada) |
| DATO | Didit (intermediario): validación RENAPER | USD 0,20 por consulta concluyente; 500 verificaciones gratis por mes | USD | https://didit.me/es/blog/argentina-renaper-dni-verification-api/ (E5021) | 2026 | media (declaración comercial) |
| DATO | Brickken: KYC adicional | €3,50 | EUR | E5007 | 2026-10-19 | alta |
| DATO | Firma digital (certificado AC ONTI con token) | sin arancel por el certificado. El token (FIPS 140-2 nivel 2) lo paga el usuario. Validez de 4 años | ARS | https://www.argentina.gob.ar/certificado-de-firma-digital-por-hardware-token (E5022) | 2026-10-19 | alta (la gratuidad es dato; el precio del token no está publicado) |
| DATO | Firma electrónica SaaS (DocuSign) | Standard USD 30/usuario/mes (100 sobres/usuario/año); Business Pro USD 45 | USD | https://ecom.docusign.com/plans-and-pricing/esignature (E5023) | 2026-10-19 | alta. Ojo: firma electrónica ≠ firma digital en la Ley 25.506 |

### 2.5 Tamaño de mercado (DATO)

| clase | parámetro | valor | unidad | fuente | fecha | certeza |
|---|---|---|---|---|---|---|
| DATO | Financiamiento total en el mercado de capitales AR, 2025 | ARS 49.151.763 M (USD 33.679 M) | ARS / USD | CNV, Informe anual de financiamiento dic-2025: https://argentina.gob.ar/sites/default/files/anual_informe_financiamiento_diciembre_2025.pdf (E5024) | 2026-02-12 | alta |
| DATO | Financiamiento PyME en el mercado de capitales, 2025 | ARS 15.295.022 M (USD 10.480 M), +7% real interanual. El 66% corresponde a pagarés | ARS / USD | ídem (E5024) | 2026-02-12 | alta |
| DATO | Fideicomisos financieros colocados, 2025 | 128 FF por ARS 2.904.541 M (USD 1.990 M) → ≈USD 15,5 M promedio por FF (inferencia) | n / USD | ídem (E5024) | 2026-02-12 | alta (el promedio es inferencia) |
| DATO | ON emitidas, 2025 | 323 por USD 17.748 M | n / USD | ídem (E5024) | 2026-02-12 | alta |
| DATO | Acciones emitidas, 2025 | USD 169 M | USD | ídem (E5024) | 2026-02-12 | alta |
| DATO | Facturas de crédito electrónicas negociadas, 2025 | 7.021 por USD 274 M | n / USD | ídem (E5024) | 2026-02-12 | alta |
| DATO (secundario) | Participación del mercado de capitales en el financiamiento pyme | <4% (96% bancario) | % | Declaración de un funcionario, https://www.sitioandino.com.ar/n/227978-la-comision-nacional-de-valores-lanzara-nuevas-herramientas-para-pymes (E5026) | 2026-07-21 | baja (cita periodística, sin base metodológica) |
| DATO | Informes mensuales CNV 2026 | **No publicados en la página «Informes del mercado de capitales»** (solo anual 2024 y 2025) | — | https://www.argentina.gob.ar/cnv/informes-del-mercado-de-capitales (E5025) | 2026-10-19 | alta (constatación) |

### 2.6 CAC y adquisición (casi todo SUPUESTO)

| clase | parámetro | valor | unidad | fuente | fecha | certeza |
|---|---|---|---|---|---|---|
| DATO (no verificable) | CAC Nubank | ≈USD 7 por cliente | USD | https://axellynch.substack.com/p/nu-holdings-nu (E5027) | 2025–26 | baja: blog sin cita primaria. Nubank no publica CAC en sus resultados. Banco masivo, no comparable con inversión en proyectos |
| DATO (no verificable) | Costo de servicio mensual por cliente activo de Nubank | ≈USD 0,8–1,0 | USD/mes | https://startups.com.br/negocios/nubank-fecha-2025-com-us-29b-em-lucro-e-roe-de-33/ (E5028) | 2026 | media |
| SUPUESTO | CAC por inversor minorista **registrado con KYC** (AR, pago digital) | 15 / 40 / 100 (optimista / base / conservador) | USD | sin fuente. Hipótesis de A5 | — | baja |
| SUPUESTO | Conversión registrado → inversor que invierte al menos una vez | 30% / 15% / 5% | % | sin fuente | — | baja |
| SUPUESTO | CAC por inversor **activo** (derivado) | ≈USD 50 / 267 / 2.000 | USD | inferencia = CAC registro / conversión | — | baja |
| SUPUESTO | CAC por emisor (originación B2B: ventas, DD inicial) | 1.500 / 4.000 / 10.000 | USD por emisor que cierra | sin fuente | — | baja |

---

## 3. Supuestos de modelado propuestos (para A5 modelo / 05_MODELOS_DE_NEGOCIO)

Todos son **SUPUESTOS** y deben validarse con el plan de entrevistas de A4.

| parámetro | conservador | base | optimista | razón / ancla |
|---|---|---|---|---|
| Monto medio por campaña (régimen PFC) | USD 150k | USD 400k | USD 1,0M | Tope legal ≈USD 2,1M (E5009). En la práctica se usa poco del tope |
| Campañas cerradas por año (año 2) | 4 | 12 | 30 | sin ancla; depende de la originación |
| Take rate al emisor (comisión de éxito) | 4% | 6% | 8% | ancla internacional 6–7,9% (E5001, E5003) |
| Fee al inversor | 0% | 1% | 2% | ancla internacional 2–3,5% (E5002, E5005). En AR puede limitar la conversión |
| Ticket medio por inversor | USD 300 | USD 800 | USD 2.000 | tope legal UVA 150k (PFC) o UVA 3k–10k (RG 1125) |
| Inversores por campaña (derivado) | 500 | 500 | 500 | = monto / ticket. **Consecuencia:** con tickets chicos hacen falta cientos de inversores por campaña, lo que dispara el CAC |
| Costo KYC por inversor | USD 1,9 | USD 1,4 | USD 0,8 | E5018, E5019 (+RENAPER ≈USD 0,04) |
| Costo legal/estructuración por emisor (FF o PFC + DD) | USD 40k | USD 20k | USD 8k | **sin fuente pública**. Ver §2.3. Pregunta prioritaria para fiduciarias y abogados |
| Default/fraude (pérdida esperada sobre el GMV, impacto reputacional) | 8% | 4% | 1% | sin fuente |
| Costo de atención por inversor activo por año | USD 12 | USD 6 | USD 3 | ancla débil en E5028 |
| Costo fijo anual de plataforma (equipo mínimo + compliance + tasas) | USD 600k | USD 350k | USD 200k | sin fuente. Incluye la tasa CNV si se registra (E5013) |

**Ejemplo de umbral (inferencia aritmética, no es dato):** con take rate total del 7% (6% emisor + 1% inversor), cada USD 1 M de GMV deja ≈USD 70k brutos. Para cubrir USD 350k de costo fijo hacen falta ≈USD 5 M de GMV por año, antes del CAC. Si el ticket medio es USD 800, eso equivale a ≈6.250 suscripciones por año. Con un CAC por inversor activo de USD 267 (base), solo la adquisición cuesta ≈USD 1,7 M. **En el escenario base el modelo no cierra si cada inversor invierte una sola vez.** Se necesita recurrencia (≥4–5 inversiones por inversor), CAC muy bajo (canal de un socio ALyC/PSAV con base existente) o un modelo B2B (SaaS o originación pagada por el estructurador). Esta sensibilidad la tiene que recalcular el modelo formal.

---

## 4. Lo que **no** se pudo obtener con fuente pública (vacíos)

- Tarifas de fiduciarias financieras, ALyC colocadores, calificadoras y estudios jurídicos para FF y ON pyme chicos: no se publican. Hay que conseguir **cotizaciones (pedido humano, fuera del alcance de este agente)**.
- Comisiones de PFC argentinas registradas y de Crowdium o similares: no hay tarifa pública. Hay que leer los contratos de adhesión.
- CAC de fintech o brokers en Argentina: no existe benchmark con fuente primaria.
- Derechos de listado y negociación de BYMA/MAV/A3 para ON pyme 2026: no se encontró el tarifario vigente en búsqueda (quedó pendiente de lectura directa de los tarifarios de los mercados).
- Precio comercial de los tokens de firma digital (Encode, Lakaut, etc.): no está publicado.
- Texto completo de la RG 1125/2026: solo se leyó el comunicado oficial.

## 5. Enlaces rotos / bloqueos

- https://wefunder.com/faq → 403. Se usó el centro de ayuda oficial (helpjuice).
- https://republic.com/help/* y https://republic.com/raise → 403 (WebFetch y curl). Se usaron los Form C de EDGAR.
- https://www.capterra.co.uk/software/1112840/Brickken → 403. Se usó la página oficial brickken.com/plans.
- https://www.brickken.com/pricing → 404 (la página real es /plans).
- https://www.boletinoficial.gob.ar/detalleAviso/primera/337307/20260109 (RG 1103/2026) → 503 en WebFetch. Se usó la Res. ME 1/2026 con anexos, descargada por curl.
- https://matbarofex.com.ar/documentos/legales/rg-cnv-942-22 → 503. Se usó el Boletín Oficial.
- https://www.argentina.gob.ar/cnv/informes/informes-de-financiamiento → 404.
- Informes mensuales CNV 2026: no aparecen en la página oficial (solo hay anuales).
