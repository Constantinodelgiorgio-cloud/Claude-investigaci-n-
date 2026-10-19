# 02 — Benchmark internacional (Frente A2)

**Fecha de revisión:** 2026-10-19 · **Frente:** A2 Benchmarks internacionales · **Alcance:** 15 modelos (EE.UU., Reino Unido, España, Luxemburgo, Brasil, Colombia, México).
**Datos fuente:** `research/frentes/A2_internacionales.csv` (mapa) y `research/frentes/A2_evidencia.csv` (E2001–E2052).

> **Advertencias de método**
> - La regulación de cada país se describe **solo** para entender el modelo. **No** se traslada a Argentina. Si un rol extranjero (funding portal, IFC, plataforma CVM 88, ERIR) se parece a una figura argentina (PFC, ALyC, PSAV), la equivalencia la tiene que confirmar el frente A3 o un abogado argentino.
> - Etiquetas: **[H]** hecho verificado en fuente primaria u oficial · **[D]** declaración comercial de la empresa · **[S]** fuente secundaria (prensa o reseña) · **[I]** inferencia del frente.
> - Republic, Wefunder, Republic Europe y Crowdcube bloquean el acceso automatizado (HTTP 403). Sus datos de comisiones y ofertas salen de registros oficiales (SEC/FINRA), de su centro de ayuda (Wefunder) o de fuentes secundarias, con la confianza indicada.
> - "Tokenizado" no implica derechos: en todos los casos los derechos del comprador surgen del **instrumento jurídico** (préstamo participativo, participación de LLC, pagaré, CCB, valor mobiliario), no del token.

## 1. Tabla resumen

| # | Modelo | País | Categoría | Tokeniza | Rol regulado (país de origen) | Registro verificado | Ticket mínimo | Monetización (publicada) | Señal reputacional |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Republic | EE.UU. | Marketplace + emisor de tokens | Parcial (Solana) | Funding portal + broker-dealer (+ATS vía INX) | Sí: FINRA/EDGAR | USD 50 (rSpaceX) | Emisor 7% + 2% en valores; inversor 2,5% [S] | Republic Note −87/90% [S]; Reg CF cae a USD 15,6M en 2024 [S] |
| 2 | Wefunder | EE.UU. | Marketplace crowdfunding | No | Funding portal Reg CF | Sí: FINRA/EDGAR | No verificable | Emisor 7,9% + admin ≤ USD 1.000/año [H] | Multa FINRA USD 1,4M (2022) [H] |
| 3 | StartEngine | EE.UU. | Marketplace + secundario | No | Funding portal + broker-dealer | Sí: FINRA/EDGAR | No verificable | Inversor 3,5% (tope USD 700); emisor 3,5% + 1–2% acciones (Reg A+) [H] | Multa FINRA USD 350.000 (2022) [H]; 1,2% de exits [S] |
| 4 | Republic Europe (ex Seedrs) | Reino Unido | Marketplace + secundario | No | FCA (declarado) | No (FCA no consultado) | No verificable | No verificable | Fusión con Crowdcube bloqueada por la CMA [S] |
| 5 | Brickken | España | SaaS de tokenización | Sí (EVM) | Ninguno (proveedor tecnológico) | No aplica | EUR 299/mes (emisor) | SaaS EUR 299–1.999/mes; whitelabel desde EUR 2.500/mes [H] | Sin sanciones halladas |
| 6 | Reental | España/EE.UU. | Emisor propio inmobiliario | Sí (Polygon) | Ley 6/2023 + ERIR (ES); Reg D/S (EE.UU.) [D] | Parcial [S] | 100 EUR/USD | No publicada | Sin advertencias CNMV halladas (búsqueda no exhaustiva) |
| 7 | RealT | EE.UU. | Emisor propio inmobiliario | Sí | No registrado como BD [D] | No | No verificable | No verificable | **Liquidación voluntaria (jul-2026), demanda municipal por 408 inmuebles** [S] |
| 8 | Securitize | EE.UU. | Infraestructura + BD/ATS + TA | Sí (multicadena) | Broker-dealer, ATS, transfer agent | Sí: EDGAR | Institucional | Emisión, administración, TA y trading | Cotiza en NYSE (SECZ) desde 02-07-2026 [S] |
| 9 | Tokeny | Luxemburgo | Infraestructura (ERC-3643) | Sí (EVM) | Ninguno (tecnología) | No aplica | Por demo | Licencia SaaS (no publicada) | Adquirida por Apex Group [H] |
| 10 | Bloxs | Brasil | Infraestructura B2B + plataforma CVM 88 | Declarado [S] | Plataforma CVM 88 | Sí: registro CVM | No verificable | Software B2B | Giro de crowdfunding minorista a B2B [H] |
| 11 | Liqi | Brasil | Tokenizadora + securitizadora | Sí | Plataforma CVM 88 (securitizadora) | Sí: registro CVM | No verificable | No publicada | Mercado de tokens de renta fija frenado por la CVM en 2023 [S] |
| 12 | Mercado Bitcoin (MB Tokens) | Brasil | Emisor/distribuidor + exchange | Sí (ERC-20) | Plataforma CVM 88; PSAV en trámite ante el BCB | Sí: registro CVM | R$ 100 | No publicada (spread/estructuración) | La CVM pidió aclaraciones (2023) [S] |
| 13 | a2censo | Colombia | Marketplace de bolsa | No | Plataforma de la BVC (SFC) | No (SPA) | COP 500.000 | Éxito ≤ 5% + mensual (dato 2020) [S] | En 2020, solo 2 de 6 campañas iniciales completas [S] |
| 14 | briq.mx | México | Marketplace inmobiliario | No | IFC autorizada por la CNBV [D] | Pendiente | MXN 500 | Emisor: dictamen MXN 17.000 + éxito ≤ 5%; inversor: ≤ 10% de rentas [H] | Sin sanciones halladas |
| 15 | Play Business | México | Marketplace crowdequity | No | IFC autorizada por la CNBV | Pendiente | No verificable | No verificable | **Suspendió nuevas inversiones** [H] |

Excluidos o no completados: **Vórtx QR Tokenizadora** (qrtokenizadora.com.br devolvió error 502 del proxy y no figura en el registro CVM de plataformas de crowdfunding; no verificado) y **Crowdcube** (403; solo se hallaron comisiones en agregadores, con confianza baja: inversor 2,49%, emisor 7%).

## 2. Fichas por modelo

### 2.1 Republic (EE.UU.)
- **URL oficial:** https://republic.com/ · Ofertas: https://republic.com/investment-opportunities · Cómo funciona: https://republic.com/help/what-is-securities-crowdfunding-1. Las tres devuelven **403** al acceso automatizado: el dominio es correcto, pero el contenido no pudo leerse.
- **Funciones:** marketplace de ofertas Reg CF, Reg D y Reg A+; SPV para acreditados (Republic Capital); productos propios tokenizados.
- **Instrumentos:** acciones, SAFE y notas de startups. **Mirror Tokens** (rSpaceX, lanzado el 25-06-2025): mínimo USD 50, tope de USD 5.000, emitido en Solana bajo Reg CF. **No** da derechos sobre acciones de SpaceX: según Ledger Insights son pagarés de RepublicX (E2018). Republic Note: token de reparto de ingresos (E2020).
- **Acceso:** minoristas bajo los límites de Reg CF según la ayuda de Republic. Reseñas de 2026 describen un giro hacia productos solo para acreditados. Hay contradicción (E2049).
- **Monetización [S]:** al emisor, 7% en efectivo más 2% en valores; al inversor, 2,5% (USD 5 a USD 250); carry de 10% a 20% en SPV (E2016).
- **Admisión de emisores:** no verificable (página 403).
- **Regulación (EE.UU.):** OpenDeal Portal LLC figura en la lista de funding portals de FINRA y en EDGAR (E2008, E2010). OpenDeal Broker LLC presenta X-17A-5 como broker-dealer (E2011). Compró INX (ATS y agente de transferencia) en abril de 2025 [S] (E2019).
- **Reputación:** el token Republic Note cayó entre 87% y 90% [S]. BBB y Trustpilot muestran quejas por reembolsos y liquidez [S]. No se hallaron sanciones SEC/FINRA contra Republic en esta revisión.
- **Métricas:** Reg CF de USD 15,6M en 2024, frente a USD 99,4M de Wefunder [S] (E2017). La métrica de Reg CF no capta la actividad para acreditados.

### 2.2 Wefunder (EE.UU.)
- **URL:** https://wefunder.com/ (403) · Ofertas: https://wefunder.com/explore (403) · Cómo funciona y comisiones: https://help.wefunder.com/ (200) y https://wefunder.helpjuice.com/getting-started-for-founders/303756-how-does-wefunder-make-money.
- **Funciones:** crowdfunding de equity y deuda para startups y pymes; SPV para agrupar inversores; servicios posteriores al cierre (reportes, impuestos del SPV).
- **Acceso:** minoristas y acreditados bajo los límites de Reg CF.
- **Monetización [H]:** 7,9% del monto captado, solo si la ronda cierra, más un cargo anual igual al menor entre USD 1.000 y 0,5% de lo captado (E2014). No cobra fee inicial.
- **Tecnología:** sin blockchain.
- **Regulación:** Wefunder Portal LLC está en la lista FINRA y en EDGAR (E2007, E2010).
- **Reputación [H]:** FINRA la multó con USD 1,4M en mayo de 2022 por superar los límites de Reg CF en unos USD 20M en 39 ofertas, solicitud indebida, comunicaciones engañosas y supervisión deficiente (E2015).
- **Métricas:** USD 983M y 2.200+ empresas, según un tercero, con datos contradictorios (E2048). Los reportes de Kingscrowd de 2025 muestran unas 200 empresas y USD 7–8,6M por mes [S].

### 2.3 StartEngine (EE.UU.)
- **URL:** https://www.startengine.com/ · Ofertas: https://www.startengine.com/explore · Cómo funciona: https://www.startengine.com/offering/how-it-works. Responden 200, pero son SPA y no se renderizan para la herramienta.
- **Funciones:** Reg CF y Reg A+, mercado secundario propio y compra de activos de SeedInvest.
- **Monetización [H, oferta específica]:** cargo al inversor de 3,5% (tope de USD 700) y, al emisor, 3,5% en efectivo más 1–2% en acciones en Reg A+ (E2022). Terceros citan 7–10% en Reg CF, sin verificar.
- **Regulación:** StartEngine Capital LLC (funding portal) y StartEngine Primary LLC (broker-dealer, X-17A-5) (E2009, E2012).
- **Reputación [H]:** multa FINRA de USD 350.000 en 2022 por contenido engañoso de emisores y conteos inexactos de inversores (E2015). Según un tercero, solo 1,2% de las empresas financiadas tuvo un evento de liquidez (E2023).
- **Métricas:** usuarios declarados de 1M, 2,1M o 2,4M según la fuente (E2050). Es un ejemplo de por qué no conviene aceptar "comunidad de millones" sin verificar.

### 2.4 Republic Europe (ex Seedrs, Reino Unido)
- **URL:** https://europe.republic.com/. https://www.seedrs.com redirige ahí; ambos devuelven 403.
- **Modelo:** equity crowdfunding con mercado secundario. Opera como Republic Europe desde el 10-07-2024, tras la compra por Republic que valuó a Seedrs en USD 100M. La CMA bloqueó la fusión previa con Crowdcube (E2021).
- **Regulación:** autorización FCA declarada, sin verificar en el registro FCA. **Comisiones:** no verificables.
- **Lección [I]:** la consolidación del sector (Seedrs → Republic, SeedInvest → StartEngine, INX → Republic) sugiere que las plataformas chicas no escalan solas.

### 2.5 Brickken (España)
- **URL:** https://www.brickken.com/ · Cómo funciona: https://www.brickken.com/asset-tokenization-platform y https://www.brickken.com/how-to-tokenize · Precios: https://www.brickken.com/plans. No publica ofertas a inversores (es B2B).
- **Funciones:** emisión de tokens de equity, deuda, crédito privado y fondos; onboarding con KYC/KYB; cap table; acciones corporativas; distribuciones; whitelabel y API.
- **Tecnología:** Ethereum, BNB Chain, Base y Polygon (E2001).
- **Monetización [H]:** Issuer Studio de EUR 299 a EUR 1.999 por mes, con tope de emisión de EUR 250K en el plan Core; whitelabel desde EUR 2.500 por mes; API a EUR 2.000 por mes más setup; KYC extra a EUR 3–3,5 (E2002). Lo legal y el gas quedan fuera.
- **Admisión:** no filtra emisores por calidad. La responsabilidad jurídica del instrumento es del emisor [S].
- **Regulación:** no declara licencia de valores; menciona ISO, EU Blockchain Sandbox y "alineación MiCA" (E2003). Opera como proveedor tecnológico.
- **Métricas [D]:** 150+ clientes y USD 660M+ de TTV, sin desglose (E2001).

### 2.6 Reental (España / EE.UU.)
- **URL:** https://www.reental.co/ · Ofertas: https://www.reental.co/properties · Cómo funciona: https://www.reental.co/ayuda y https://www.reental.co/faqs.
- **Instrumento [H]:** en España, préstamo participativo tokenizado y, desde fines de 2025, obligaciones bajo la Ley 6/2023 con ERIR. En EE.UU., participaciones de LLC bajo Reg D (acreditados) y Reg S (no residentes). Rendimientos en USDT (E2005, E2006).
- **Acceso:** minoristas globales, mínimo 100 EUR/USD; KYC/AML; wallet propia (MetaMask y similares).
- **Liquidez:** venta P2P solo a otro usuario acreditado en la plataforma (E2005).
- **Monetización:** comisiones no publicadas. Se presume margen de estructuración y gestión [I].
- **Tecnología:** Polygon, más el token propio RNT y el servicio RNT Lend.
- **Regulación:** primera emisión bajo Ley 6/2023 de EUR 322.500 (3.225 tokens), inmueble en Málaga, formalizada ante la CNMV en dic-2025 [S] (E2006). Sin número de registro ni ERIR identificada.
- **Reputación:** no se hallaron advertencias de la CNMV en la búsqueda abierta. Falta consultar el buscador oficial (E2052).
- **Métricas [D]:** 128 proyectos, USD 124M+ tokenizados y 16,44% de rentabilidad media en proyectos cerrados, sin auditar (E2004).

### 2.7 RealT (EE.UU.) — caso de fracaso
- **URL:** https://realt.co/ redirige (2026-10-19) a realtusa.pulse.is, que indica que el servicio no está abierto a personas de EE.UU. y que RealToken Inc. no es broker-dealer ni asesor registrado (E2026). Ofertas: https://realt.co/marketplace/, que también redirige.
- **Modelo:** tokens que representan participaciones en LLC dueñas de casas de alquiler en Detroit, vendidos sobre todo a inversores no estadounidenses, con rentas distribuidas on-chain.
- **Problemas [S, medios locales]:**
  - 02-07-2025: Detroit demandó a RealT, a sus fundadores y a 165 entidades por **408 inmuebles** sin certificado de cumplimiento, con deudas de impuestos y multas. Un juez prohibió cobrar alquileres y desalojar en propiedades sin certificado (E2024).
  - Abril de 2026: se designó un fiduciario especial con la última palabra sobre las ventas.
  - 02-07-2026: RealT anunció su **liquidación voluntaria** y la venta de ~700 inmuebles. Había captado ~USD 140M. Unos 400 inversores se suman a una acción legal en Francia (E2025).
- **Lección clave [I]:** el token no protegió al inversor del riesgo operativo (gestión de inmuebles, administradores, impuestos), del riesgo de contraparte del sponsor ni del riesgo jurisdiccional. La blockchain registraba la tenencia de forma perfecta mientras el activo subyacente se deterioraba.

### 2.8 Securitize (EE.UU.)
- **URL:** https://securitize.io/ · Ofertas: https://securitize.io/invest · Cómo funciona: https://securitize.io/how-it-works. Responden 200, pero son SPA; WebFetch devolvió 404 en how-it-works.
- **Funciones:** emisión y administración de fondos tokenizados (BUIDL de BlackRock y otros), agente de transferencia y ATS para negociación secundaria.
- **Regulación [H]:** Securitize Markets LLC (broker-dealer, con X-17A-5 y FOCUS) y Securitize Transfer Agent LLC (TA-1/TA-2) (E2013).
- **Hitos [S]:** fusión con el SPAC Cantor Equity Partners II; cotiza en NYSE como SECZ desde el 02-07-2026; tokenizó sus propias acciones en Solana y Avalanche (E2027). Ingresos de USD 19,5M en el 1T 2026 y USD 4.000M+ de AUM tokenizado (E2028).
- **Lección [I]:** el caso de éxito en volumen es **institucional**, con licencias completas (BD, ATS y TA) y un ancla de demanda (fondos de gestoras globales). No es crowdfunding pyme.

### 2.9 Tokeny (Luxemburgo)
- **URL:** https://www.tokeny.com/ · Cómo funciona: https://www.tokeny.com/how-it-works/ · Plataforma: https://www.tokeny.com/t-rex-platform/.
- **Funciones:** T-REX Platform y T-REX Engine; estándar abierto **ERC-3643** (tokens con identidad y reglas de transferencia on-chain); compatible con EVM.
- **Monetización:** licencias por demo, sin precios publicados.
- **Propiedad [H]:** Apex Group tomó participación mayoritaria en mayo de 2025 (E2030). Facturación 2023 de EUR 1,21M según registro luxemburgués [S].
- **Métricas [D]:** USD 32.000M tokenizados y 120+ clientes (E2029). Ese valor corresponde a activos de terceros emitidos con su tecnología, no a capital captado.
- **Lección [I]:** la infraestructura de tokenización se commoditiza y termina integrada en administradores de fondos. Con ingresos chicos frente al "valor tokenizado", es un mal negocio independiente.

### 2.10 Bloxs (Brasil)
- **URL:** https://bloxs.com.br/ (redirige a https://site.bloxs.com.br/pt-BR). La página de crowdfunding (https://site.bloxs.com.br/pt-BR/crowdfunding) da **404**. Alta: https://app.bloxs.com.br/signup/company (no usada).
- **Registro [H]:** Bloxs Capital Market Solutions Ltda. (Altxs Investimentos) es plataforma CVM 88 "Em Funcionamento Normal" desde 2018 (E2032).
- **Modelo actual [H]:** infraestructura para que *wealth managers* estructuren y distribuyan CRI, CRA y debêntures, con coordinadora, securitizadora y gestora propias. El sitio aclara que Bloxs Tech no es institución financiera ni ofrece valores (E2035). Prensa: relanzamiento como marketplace de operaciones estructuradas y foco en Drex [S].
- **Lección [I]:** un pionero del crowdfunding de inversión en Brasil **pivotó de minorista directo a B2B con distribución por asesores**. Es una señal fuerte sobre dónde está el dinero (estructuración y distribución) y dónde no (CAC minorista).

### 2.11 Liqi (Brasil)
- **URL:** https://www.liqi.com.br/ · Ofertas: https://tokens.liqi.com.br/ · Cómo funciona: https://www.liqi.com.br/faq.
- **Funciones [D]:** securitizadora, distribución por marketplace propio, CaaS (cripto y tokens para terceros) y stablecoin BRLD. Tokeniza CCB y recebíveis (E2036).
- **Registro [H]:** LIQI SECURITIZADORA S.A. es plataforma CVM 88 desde el 30-07-2024 (E2033). La regulación del BCB declarada no está verificada.
- **Comisiones:** no publicadas. **Blockchain:** no identificada en el sitio.
- **Métricas [S]:** R$ 22M tokenizados bajo CVM 88, según InvestNews (fecha no clara).

### 2.12 Mercado Bitcoin — MB Tokens / Renda Fixa Digital (Brasil)
- **URL ofertas y funcionamiento:** https://www.mercadobitcoin.com.br/oferta-publica/renda-fixa-digital.
- **Instrumento:** tokens ERC-20 que representan precatorios, consorcios y recebíveis. Mínimo de R$ 100. Sin cobertura del FGC. MB no garantiza retorno (E2038).
- **Registro [H]:** MB Securitização e Distribuição S.A. ("MB TOKENS") es plataforma CVM 88 desde 2020 (E2034). La PSAV está en proceso de autorización ante el BCB.
- **Reputación [S]:** en 2023 la CVM cuestionó las "criptos de renta fija". Luego encuadró los tokens de recebíveis como valores mobiliarios, con un tope de R$ 15M bajo la Res. 88 (E2039). La Res. 88 está en reforma: la consulta cerró el 23-01-2026 (E2040).
- **Métricas [D]:** ~R$ 1.000M distribuidos en 2025, ~350 emisiones y 30% del resultado proveniente de tokenización (E2037).
- **Lección [I]:** el caso latinoamericano de mayor volumen tiene **base de clientes cripto preexistente** (bajo CAC) y producto de **renta fija corta y estandarizada**, no equity pyme.

### 2.13 a2censo (Colombia)
- **URL:** https://a2censo.com/ · Cómo funciona: https://a2censo.com/como-funciona. Responde 200, pero es SPA sin contenido y WebFetch devuelve 403. Campañas no visibles.
- **Modelo:** plataforma de financiación colaborativa **de la Bolsa de Valores de Colombia**, integrada al hub regional nuam. Ofrece deuda, acciones (desde 2024) y notas convertibles.
- **Métricas [S]:** COP 111.300M para 193 empresas en 217 oportunidades; 14.754 inversores, 98% personas humanas; ticket promedio de COP 2,2M; mínimo de COP 500.000 (jul-2025, E2041).
- **Monetización [S, 2020]:** comisión de éxito de hasta 5%, cargo mensual y comisión del fondo de garantías (E2042).
- **Reputación [S]:** en la primera tanda de 2020, solo 2 de 6 campañas completaron su meta (E2042).
- **Lección [I]:** aun con la marca de la bolsa y un fondo de garantías, el volumen acumulado en ~6 años es modesto, del orden de USD 25–30M según el tipo de cambio [I]. La demanda minorista es el cuello de botella.

### 2.14 briq.mx (México)
- **URL:** https://www.briq.mx/ · Ofertas: https://www.briq.mx/proyectos · Cómo funciona: https://www.briq.mx/como-invertir · Selección: https://www.briq.mx/proceso-seleccion · Comisiones: https://www.briq.mx/regulacion/comisiones.
- **Instrumentos:** deuda senior y copropiedad inmobiliaria. Mínimo de MXN 500. Sin blockchain.
- **Monetización [H]:** al desarrollador, dictamen legal de MXN 17.000 + IVA y comisión de éxito de hasta 5%. Al inversor, solo sobre lo cobrado: hasta 10% de rentas y hasta 2% de intereses o capital (E2044).
- **Admisión:** proceso de selección publicado. Si el desarrollador no paga, se ejecuta el inmueble de respaldo [D].
- **Regulación (México):** IFC autorizada por la CNBV según el sitio (E2043); ampliada en jun-2026 según prensa (E2051). Falta verificar el Padrón CNBV.
- **Métricas [D]:** MXN 2.800M+ invertidos y 595 campañas terminadas y pagadas (E2045).
- **Lección [I]:** es el comparable regional más sano: **sin token**, nicho único (inmobiliario con garantía real), tarifario transparente y costo de admisión cobrado al emisor.

### 2.15 Play Business (México) — caso de repliegue
- **URL:** https://playbusiness.mx/ (redirige a /entrar) · FAQ: https://playbusiness.mx/faqs.
- **Modelo:** crowdequity y regalías para startups. Autorizada como IFC (DOF 30-09-2021) [S] (E2046).
- **Estado [H]:** "ha decidido suspender temporalmente nuevas inversiones" y se concentra en su portafolio activo (E2047).
- **Lección [I]:** incluso con licencia, el **equity de startups para minoristas** no se sostuvo. Es una alerta directa para un marketplace multisectorial de proyectos productivos en Argentina.

## 3. Lecciones transferibles a Argentina

Son patrones de negocio y producto, no normas.

1. **Cobrar al emisor por éxito y por admisión.** El rango observado de comisión de éxito es 5–9%: briq ≤ 5%, a2censo ≤ 5%, Republic 7% + 2%, Wefunder 7,9%. Un cargo fijo de admisión o dictamen (briq, MXN 17.000) filtra a los emisores poco serios y cubre la debida diligencia. Hay que validar con A4/A5 si una pyme argentina acepta un costo de ese orden.
2. **Los costos al inversor existen, pero son chicos y ligados al flujo:** 2,5–3,5% al invertir en EE.UU. o un porcentaje sobre lo cobrado (briq). Cobrar sobre lo cobrado alinea incentivos.
3. **El volumen está en instrumentos cortos, estandarizados y de renta fija** (MB, Liqi, briq deuda senior), no en equity de startups (Play Business suspendido, exits de 1,2% en StartEngine [S]).
4. **La distribución pesa más que la tecnología.** MB tiene base cripto propia; a2censo tiene la marca de la bolsa; Bloxs pivotó a distribuir vía *wealth managers*. Un marketplace sin canal propio compite por CAC minorista.
5. **El pivot B2B es recurrente** (Bloxs, Brickken, Tokeny, Securitize institucional). Las variantes M1 y M2 del mandato deberían evaluar vender herramientas de originación, *data room* y reporting a ALyC, fiduciarias o PFC antes que captar minoristas.
6. **La infraestructura de tokenización es un commodity barato.** Brickken publica planes desde EUR 299 por mes y ERC-3643 es estándar abierto. Desarrollar tecnología on-chain propia no diferencia; conviene integrarla o alquilarla si se demuestra valor (frente A7).
7. **La reputación depende del activo subyacente y del sponsor, no del token** (RealT). Antes de listar hacen falta debida diligencia del emisor, control de gestión de activos, cuenta escrow, administrador independiente y plan de salida o liquidación.
8. **Publicar métricas auditables.** Las cifras de marketing son contradictorias (StartEngine con 1M a 2,4M de usuarios, Wefunder) o no definidas ("reentels", TTV). Un diferencial argentino posible es reportar a la vista tasas de default, campañas fallidas y pagos efectuados por proyecto, al estilo del desglose de briq: 595 pagadas y 418 vigentes.
9. **Liquidez secundaria marginal.** Las ventas P2P restringidas (Reental) y los secundarios con costos de ~8,5% ida y vuelta (StartEngine [S]) muestran que prometer liquidez es riesgoso. Coincide con la cautela sobre M3.
10. **Las sanciones vinieron por marketing y límites, no por tecnología.** Las multas FINRA a Wefunder y StartEngine fueron por superar topes, comunicaciones engañosas y contenido de emisores no controlado. Un portal M0/M1 en Argentina necesita control editorial de lo que publica el emisor. A3 debe definir si eso lo hace "promoción" regulada.
11. **Las plataformas se cancelan.** En Brasil, 48 de 154 registros de crowdfunding en la CVM están cancelados: 31% de 154, o 35% de las 137 que alguna vez obtuvieron registro (E2031, E9018). La tasa de mortalidad debe entrar en los kill criteria de A8.

## 4. Lo que NO es transferible

- **Figuras regulatorias.** Funding portal Reg CF, Reg D/Reg A+/Reg S, broker-dealer FINRA, ATS (EE.UU.); FCA (Reino Unido); Ley 6/2023 y ERIR, MiCA y régimen piloto DLT (España/UE); plataforma CVM 88 y PSAV del BCB (Brasil); IFC bajo la Ley Fintech (México); financiación colaborativa SFC (Colombia). Ninguna equivale automáticamente a PFC, ALyC o PSAV ante la CNV argentina. La matriz es de A3.
- **Topes y límites por inversor o emisor** (USD 5M en Reg CF, R$ 15M en CVM 88): no aplican.
- **Exenciones para "no residentes"** que usaban RealT y Reental (Reg S). Ofrecer a residentes argentinos desde una estructura extranjera no resuelve la oferta pública local.
- **Profundidad de mercado y demanda:** la base de 2,1M+ usuarios de StartEngine, los fondos de BlackRock en Securitize o la base cripto de MB no tienen equivalente verificable en Argentina.
- **Stablecoins y rendimientos en USDT** (Reental) o stablecoin propia (Liqi BRLD): su tratamiento cambiario, fiscal y regulatorio en Argentina queda para A3.
- **Tratamiento fiscal** (exención de IR de hasta R$ 35.000 mensuales en Brasil, retención de 19% en España).
- **Bolsa como operador** (a2censo/BVC): depende de la voluntad de BYMA/MAV, no replicable por una startup.

## 5. Enlaces rotos o no legibles (2026-10-19)

| URL | Resultado | Nota |
|---|---|---|
| https://republic.com/ (y /investment-opportunities, /help/…, /learn/investors/commission) | 403 | Antibot. Datos tomados de EDGAR/FINRA y fuentes secundarias |
| https://wefunder.com/ (y /faq, /explore, /raise) | 403 | Antibot. Se usó help.wefunder.com / helpjuice |
| https://www.seedrs.com → https://europe.republic.com/ | 403 | Redirección verificada |
| https://www.crowdcube.com/ y /explore/investment-opportunities | 403 | Modelo no incluido en el benchmark |
| https://qrtokenizadora.com.br/ | 502 (proxy CONNECT) | Vórtx QR no verificada |
| https://site.bloxs.com.br/pt-BR/crowdfunding | 404 | La página de crowdfunding ya no existe |
| https://securitize.io/how-it-works | 200 con curl, 404 con WebFetch (SPA) | Contenido no legible |
| https://a2censo.com/ y /como-funciona | 200 con curl (SPA vacía), 403 con WebFetch | Datos desde prensa |
| https://www.startengine.com/ | 200 (SPA vacía para la herramienta) | Datos desde EDGAR |
| https://realt.co/ → realtusa.pulse.is | 200 | Redirección a una landing que bloquea a usuarios de EE.UU. |
| https://republic.com/learn/investors/commission | 403 | Comisiones de Republic sin verificar en fuente primaria |

## 6. Pendientes para A9 y A3
- Verificar en el Padrón CNBV a briq.mx y Play Business, en el registro FCA a Republic Europe y en BrokerCheck a OpenDeal Broker, StartEngine Primary y Securitize Markets.
- Consultar el buscador de advertencias de la CNMV para Reental y la ERIR de su emisión.
- Obtener del 8-K de Securitize las cifras de tokenización y de ingresos.
- Confirmar las comisiones de Republic en fuente primaria (bloqueada).
- Revisar el expediente judicial de Detroit contra RealT para cifras de inversores y escrow (hoy de fuentes secundarias divergentes).
