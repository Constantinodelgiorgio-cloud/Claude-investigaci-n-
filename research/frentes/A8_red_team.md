# A8: red team de negocio

**Fecha de ejecución:** 2026-10-19 (Argentina) · **Frente:** A8 · **Objetivo:** intentar falsar H0.
**H0:** existe un problema de intermediación/distribución para proyectos productivos tokenizados en Argentina, y un marketplace que opere con socios autorizados podría resolverlo.
**Evidencia:** `research/frentes/A8_evidencia.csv` (E8001–E8045).
**Convención:** **[H]** es un hecho verificado con URL. **[D]** es una declaración comercial o una cifra de terceros sin verificación primaria. **[I]** es una inferencia de A8. **[O]** es una opinión.

---

## 0. Veredicto del red team

H0 **no queda falsada del todo**, pero queda **seriamente debilitada en su formulación actual**. Los resultados son estos:

1. **El problema "de distribución" no está demostrado.** La distribución minorista masiva ya existe: 12,3 millones de personas tienen cuenta comitente y unas 1,09 millones de cuentas operan cada mes [H, E8004]. Además, en 2025 las PyMEs captaron entre USD 10.212 y 10.480 millones en el mercado de capitales con instrumentos convencionales [H/D, E8001, E8002]. Si hay un problema, parece estar en la **originación y la calidad crediticia de emisores chicos**, no en la distribución. **[I]**
2. **La tokenización no muestra valor incremental verificable para el emisor argentino de hoy.** No se encontró ningún caso argentino con monto tokenizado colocado y público bajo el régimen CNV [H, E8007, E8011].
3. **La evidencia global sobre liquidez secundaria y fracasos de plataformas es mayoritariamente negativa** [H, E8013–E8022].
4. **Evidencia a favor de H0 que hay que reconocer:** existe un registro declarado de demanda minorista a pequeña escala. Landtoken declara más de USD 850 mil y más de 200 inversiones, con ticket desde USD 100 [D, E8012]. También existe un impulso regulatorio fuerte (RG 1125, 1150 y 1165 de 2026) [H, E8005, E8007, E8009]. Ninguna de las dos cosas prueba que haya un negocio de marketplace.

---

## 1. Razones concretas para NO emprender (12)

### R1. El canal de distribución ya existe y está dominado por incumbentes con escala
- **Evidencia [H]:** según BYMA, al 31/05/2026 hay más de 12,3 millones de personas con cuenta comitente, 24,6 millones de cuentas, unas 1,09 millones de cuentas operativas por mes y más de 1 millón de tenedores de CEDEARs (E8004).
- **Evidencia [H]:** el régimen de tokenización prevé que los inversores operen por ALyC, bancos y PSAV (E8010, E8011).
- **[I]:** un marketplace nuevo compite en adquisición de inversores con ALyC y billeteras que ya tienen KYC hecho y saldo disponible. Su CAC sería mayor y su diferenciación menor.
- **Qué revertiría la objeción:** entrevistas (A4) en las que al menos el 60% de los inversores objetivo digan que *no encuentran* proyectos productivos en sus ALyC y estén dispuestos a abrir una cuenta nueva por eso. Otra vía: que los ALyC declaren que no quieren originar pymes chicas y prefieran recibirlas referidas.

### R2. Las PyMEs solventes ya tienen financiamiento más barato y estandarizado
- **Evidencia [H/D]:** en 2025 el financiamiento PyME fue de USD 10.480 millones según la CNV citada por BAE (E8001), o de USD 10.212 millones según BCSF. En la cifra de BCSF, el pagaré bursátil explica el 66,1% (E8002).
- **Evidencia [H]:** la ON PyME CNV Garantizada de Vitalcan (hasta USD 10 M) estimó gastos totales de alrededor del 1,03% del monto (E8003).
- **[I]:** para la PyME con aval de SGR y balance auditado, la tokenización suma costo y novedad sin reducir la tasa. El emisor que *no* consigue aval es justamente el de mayor riesgo (ver R6).
- **Qué revertiría la objeción:** tres cotizaciones reales en las que una emisión tokenizada de USD 200–500 mil cueste, todo incluido, igual o menos que un pagaré avalado equivalente (honorario SGR + agente + tasa). Otra vía: que al menos 5 PyMEs con acceso a SGR declaren que prefieren el canal tokenizado y digan por qué.

### R3. La economía de la estructuración no cierra en tickets chicos
- **Evidencia [H]:** el 1,03% de Vitalcan corresponde a un techo de USD 10 M (E8003). Los costos fijos (legales, fiduciario, auditoría, calificación) no escalan hacia abajo.
- **Evidencia [D]:** el software de tokenización suma costo propio. Brickken, por ejemplo, arranca en unos EUR 3.000 por año, más fees de creación y cierre y el gas on-chain (E8039).
- **Evidencia [H]:** el crowdfunding de la RG 1125 limita a cada inversor a UVA 3.000 por emisión (unos ARS 6,47 M con la UVA a ARS 2.156,58) y a UVA 10.000 en total, además de un tope del 5% de su patrimonio por emisión (E8005, E8006).
- **[I]:** con un ticket real promedio muy por debajo del tope, una emisión de USD 300 mil necesita cientos de inversores. El costo de KYC y atención por inversor, más un costo fijo de estructuración que A8 estima (sin verificar) en USD 15–40 mil, puede consumir entre el 5% y el 15% de lo captado. **Esta estimación es una hipótesis y requiere cotizaciones (K3).**
- **Qué revertiría la objeción:** cotizaciones firmes de fiduciaria/ALyC/PFC con costo total menor al 3% para una emisión de USD 300 mil.

### R4. El crowdfunding regulado lleva 9 años con uso marginal y sin estadística pública
- **Evidencia [H]:** la Ley 27.349 es de 2017, la RG 717 de 2017/2018 y la RG 942 de 2022. Ni la nota oficial de la RG 1125 ni la de la RG 1150 informan cantidad de proyectos, montos o plataformas (E8005, E8007, E8043).
- **[D/O]:** en fuentes secundarias aparece la afirmación de que hubo una sola PFC registrada en 2022 y de que el régimen tiene "muy poco uso". **No se pudo verificar en fuente oficial.** El buscador CNV de la categoría "PLAT. FINAN. COLECT." exige enviar un formulario, cosa que no se hizo por protocolo.
- **[I]:** si en 9 años el crowdfunding regulado no generó volumen visible, el cuello de botella no era tecnológico (la tokenización no lo resuelve). Probablemente era de oferta de proyectos, de demanda o de costo.
- **Qué revertiría la objeción:** datos oficiales o estados contables de PFC con un monto acumulado relevante (por ejemplo, más de USD 20 M captados en los últimos 24 meses) y crecimiento interanual.

### R5. La liquidez secundaria prometida por la tokenización no aparece en la práctica
- **Evidencia [H]:** Mafrur (2025) describe bajo volumen, tenencias largas, pocas direcciones activas y negociación secundaria mínima en los RWA (E8022).
- **Evidencia [H]:** cuando tZERO abrió su token a minoristas, el volumen diario volvió a menos de USD 15.000. Overstock reconoció en su 10-K un trading "extremadamente limitado" (E8017, E8020).
- **Evidencia [H]:** los tokens de RealT se venden muy por debajo de su valor original (E8014).
- **Evidencia [D]:** el inmobiliario tokenizado global representa una fracción muy chica del total de RWA, del orden de USD 0,2 mil M frente a USD 22–31 mil M (E8023).
- **[I]:** prometer liquidez sería engañoso y legalmente riesgoso. Sin liquidez, el producto compite como un instrumento ilíquido de largo plazo contra cauciones al 19–23% TNA con liquidez diaria (E8031).
- **Qué revertiría la objeción:** un market maker o un ALyC dispuesto a contratar liquidez con spreads y profundidad mínimas, o datos de rotación secundaria superiores al 10% anual en tokens comparables.

### R6. Selección adversa estructural e incentivos perversos de la plataforma
- **Evidencia [H]:** en crowdfunding, el ingreso masivo de proyectos de baja calidad sin aumento de demanda redujo el éxito promedio (Geva et al., E8035).
- **Evidencia [H]:** en Crowdcube fracasó el 18% de las empresas financiadas entre 2011 y 2015, y ninguna de las que tenían inversores calificados iniciales (Signori y Vismara, E8034).
- **[I]:** si la plataforma cobra por colocación, gana más cuanto más coloca, no cuanto mejor rinden los proyectos. Los emisores que llegan son los que no consiguieron SGR, banco ni ALyC (E8045).
- **Contexto [H/D]:** la mora del descuento de documentos se cuadruplicó hasta el 2% y en diciembre de 2025 se rechazaron 119.285 cheques (E8030).
- **Qué revertiría la objeción:** una cohorte piloto en la que el fee dependa de la performance (fee diferido o *skin in the game* de la plataforma) y la tasa de aprobación tras due diligence sea de al menos el 30% de los emisores postulados, con estados contables auditados.

### R7. Riesgo reputacional: "token" e "inversión productiva" se asocian en Argentina a fraudes recientes
- **Evidencia [H]:** Generación Zoe prometía 7,5% mensual en USD. Hubo condenas de 12 años (Goya) y 11 años (Salta), y la **CNV absolvió a la empresa por falta de competencia** porque no se operaron valores negociables (E8024, E8025).
- **Evidencia [H/D]:** en $LIBRA, el 86% de los traders perdió USD 251 M según Nansen, unos USD 99 M de liquidez fueron retirados, y una comisión parlamentaria concluyó que los hechos son compatibles con una presunta estafa (E8026, E8027).
- **Evidencia [H]:** hubo fraudes con fideicomisos inmobiliarios: en La Plata, más de USD 20 M y 160 damnificados en 12 obras, y en el caso Induplack, más de 200 denuncias (E8028, E8029).
- **[I]:** el marketplace hereda el riesgo reputacional de cada emisor. Basta un solo fraude o default listado para destruir la marca. La experiencia de Zoe muestra que el inversor tiene escaso recurso regulatorio cuando el instrumento queda fuera del perímetro.
- **Qué revertiría la objeción:** un estudio de percepción (A4) con al menos 200 inversores objetivo que muestre confianza mayoritaria en "proyecto productivo + entidad CNV", y no rechazo a "token".

### R8. Cambio regulatorio muy rápido y sandbox con fecha de vencimiento
- **Evidencia [H]:** al menos 10 resoluciones relevantes en unos 30 meses. Entre ellas: RG 994/2024, 1058/2025, 1060, 1069, 1081 y 1087/2025, y 1125, 1137, 1150, 1165 y 1172/2026 (E8005–E8010).
- **Evidencia [H]:** el sandbox de tokenización vence el 31/12/2027 (E8007).
- **[I]:** el diseño del producto puede quedar obsoleto, o volverse no conforme, en meses. A la vez, cada liberalización baja la barrera de entrada de competidores. Por ejemplo, desde la RG 1087 no es obligatorio listar en un mercado si el 100% de la emisión es digital (E8010). Hay riesgo político de reversión tras $LIBRA y en el ciclo electoral 2027 **[O]**.
- **Contraejemplos [H]:** Neufund cerró en 2022 por incertidumbre regulatoria pese a haber canalizado EUR 20 M de 11.000 inversores (E8016). En México, plataformas de fondeo colectivo no obtuvieron autorización de la CNBV (E8036). En Brasil, la CVM emitió una stop order sobre tokens de Mercado Bitcoin (E8037, sin verificar por un 403).
- **Qué revertiría la objeción:** que la CNV convierta el sandbox en régimen permanente antes del piloto, junto con un dictamen de un abogado especialista que confirme la estabilidad del encuadre M1.

### R9. Dependencia de socios autorizados que pueden desintermediar al marketplace
- **Evidencia [H]:** la RG 1165/2026 crea una nueva matriz de compatibilidades. Los agentes pueden acumular registros, como ADCVN más fiduciario financiero (E8009).
- **[I]:** en M1, el socio regulado (ALyC/PFC/fiduciaria) es dueño del cliente, del KYC y de los fondos. Si el marketplace origina bien, el socio puede internalizarlo. Si origina mal, el socio lo abandona. El poder de negociación del marketplace es bajo.
- **Qué revertiría la objeción:** contratos con exclusividad o *non-circumvention* por al menos 24 meses y revenue share del 30% o más, firmados por al menos 2 socios.

### R10. El costo de oportunidad del inversor es alto y los productos rivales son líquidos
- **Evidencia [H]:** la caución a 1 día ronda el 19% TNA y a 4 días el 23% TNA (9/10/2026). El plazo fijo paga entre 16% y 23% TNA. La inflación es de 1,9% mensual y 33,4% interanual (E8031–E8033).
- **[I]:** las tasas reales son negativas o cercanas a cero, y eso empuja al inversor a buscar rendimiento. Eso favorece la demanda, pero también la de esquemas Ponzi (R7). Un proyecto productivo ilíquido tiene que pagar una prima alta que, otra vez, selecciona riesgo.
- **Qué revertiría la objeción:** que el piloto muestre inversores aceptando rendimientos esperados con prima de 300 pb o menos sobre ON PyME comparables, por razones no financieras (impacto, cercanía, sector).

### R11. Los fracasos globales del modelo plataforma de tokenización son la regla, no la excepción
- **Evidencia [H]:** RealT pasó de unos 700 inmuebles y alrededor de USD 140 M captados (USD 94 M según Outlier) a una demanda municipal, la suspensión de distribuciones (feb-2026), un fiduciario designado (abr-2026), una liquidación voluntaria anunciada (2/7/2026) y un escrow de unos USD 640 mil para 14–22 mil inversores (E8013–E8015).
- **Evidencia [H]:** tZERO perdió USD 35,5 M en 9 meses de 2020 y recibió una multa de la SEC de USD 800 mil (E8018, E8019). Harbor fue absorbida por BitGo con adopción lenta (E8021). Neufund cerró (E8016).
- **[I]:** el patrón común es poco volumen, costo regulatorio fijo alto y riesgo operativo del activo subyacente (gestión de inmuebles). Ese riesgo no lo resuelve la tecnología.
- **Qué revertiría la objeción:** un benchmark (A2) que identifique al menos 3 plataformas de tokenización o crowdfunding de deuda/equity pyme rentables y con más de 3 años de operación en mercados emergentes.

### R12. Mercado chico y concentración de emisores
- **Evidencia [D]:** a nivel global, el RWA tokenizado se concentra en Treasuries y crédito privado institucional, y el real estate y las pymes son marginales (E8023).
- **Evidencia [H]:** en Argentina no hay monto tokenizado colocado público bajo el régimen CNV (E8011).
- **[I]:** un marketplace "multisectorial" arranca con pocos emisores. Que 2 o 3 emisores representen más del 50% del volumen expone al marketplace a un default o fraude concentrado y a un poder de negociación del emisor.
- **Qué revertiría la objeción:** un pipeline de al menos 15 emisores calificados con LOI y ningún emisor por encima del 25% del volumen esperado.

---

## 2. Condiciones que invalidan el proyecto (si se cumple cualquiera, NO-GO para M1/M2)

1. Un abogado especialista concluye que derivar inversores con CTA o publicar ofertas con condiciones exige un registro propio (ALyC, AAGI o PFC) cuyo costo y plazo superan los USD 150 mil o los 9 meses. En ese caso queda solo M0, y hay que revisar si M0 genera ingresos.
2. Ningún socio autorizado acepta un contrato de referral y revenue share con *non-circumvention*.
3. El costo total cotizado para una emisión de USD 300 mil supera el 6% del monto.
4. Menos del 30% de los emisores postulados pasan una due diligence mínima (balance auditado, flujo demostrable, ausencia de deuda fiscal o previsional significativa, garantía o aval).
5. La demanda declarada no se convierte: menos del 5% de la lista de espera completa la precalificación con un ticket indicado.
6. La CNV no convierte el sandbox en régimen permanente, o restringe a minoristas, antes de la fecha de lanzamiento.
7. Aparece un fraude o default material en un proyecto listado durante el piloto.

(Los umbrales cuantificados y fechados están en `research/08_RIESGOS_Y_KILL_CRITERIA.md`.)

---

## 3. Contraejemplos documentados (con URL)

| Caso | Ámbito | Qué pasó | Lección para H0 | Fuente |
|---|---|---|---|---|
| RealT | EE.UU., inmuebles tokenizados | Demanda de Detroit por más de 400 inmuebles, TRO sobre alquileres, suspensión de distribuciones, liquidación voluntaria en 2026 | Token ≠ protección: el riesgo está en el activo y en el gestor | [Yahoo/TRO](https://www.yahoo.com/news/articles/judge-bars-real-token-collecting-100438516.html), [BridgeDetroit](https://www.bridgedetroit.com/?p=231204), [Crypto Briefing](https://cryptobriefing.com/realt-crypto-real-estate-collapse/) |
| tZERO | EE.UU., ATS de security tokens | Volumen diario de minoristas menor a USD 15 mil, pérdidas, multa SEC de USD 800 mil | Licencia ≠ liquidez, y la licencia trae costo de compliance | [The Block 2019](https://www.theblock.co/research/tokenization/tzeros-security-token-now-available-to-retail-but-they-arent-biting-37370), [The Block 2022](https://www.theblock.co/linked/129803/tzero-settles-with-sec-over-late-filings-under-ats-rules) |
| Neufund | Alemania | Cierre en 2022 tras EUR 20 M y 11 mil inversores, sin licencia | Tracción no alcanza si no hay licencia | [Crowdfund Insider](https://www.crowdfundinsider.com/?p=185572) |
| Harbor | EE.UU. | Emisión emblemática cancelada, absorbida por BitGo | Adopción lenta, consolidación | [The Block](https://www.theblock.co/post/56298/bitgo-acquires-token-platform-harbor-to-expand-into-the-digital-securities-space) |
| Generación Zoe | Argentina | Ponzi con promesa de 7,5% mensual, condenas penales, CNV sin competencia | Brecha de perímetro y desconfianza | [Chequeado](https://chequeado.com/el-explicador/generacion-zoe-las-claves-de-la-causa-en-la-que-leonardo-cositorto-fue-condenado-por-asociacion-ilicita-y-estafa-en-corrientes/) |
| $LIBRA | Argentina/global | Retiro de unos USD 99 M de liquidez, USD 251 M en pérdidas | "Token" queda asociado a estafa en la opinión pública | [Benzinga](https://www.benzinga.com/25/02/43839293/entitied-tied-to-libra-token-creator-reportedly-removed-99-million-in-liquiditytraders-lost-over-250-million-in-scam), [BAE](https://www.baenegocios.com/politica/Caso-LIBRA-elevan-el-informe-final-y-se-abre-una-jugada-decisiva-en-la-causa-20251118-0017.html) |
| Fideicomisos La Plata | Argentina | 12 obras paralizadas, más de USD 20 M, presunta caja única | El fideicomiso no evita el desvío si no hay control independiente | [La Nación](https://www.lanacion.com.ar/seguridad/calculan-que-llega-a-us20-millones-la-presunta-megaestafa-inmobiliaria-en-la-plata-nid20012026/) |
| Induplack | Argentina | Más de 200 denuncias, 5 detenidos, departamentos de pozo | Ídem | [Perfil](https://www.perfil.com/noticias/policia/mas-de-200-denuncias-y-5-detenidos-en-una-megaestafa-con-departamentos-de-pozo-estamos-hablando-de-mas-de-us20-millones.phtml) |
| Fintech México | México | Plataformas de fondeo colectivo sin autorización CNBV | El filtro regulatorio elimina jugadores | [LatamFintech](https://www.latamfintech.co/articles/cinco-fintechs-mexicanas-han-sido-rechazadas-para-obtener-su-autorizacion-por-parte-de-la-cnbv) |

**Evidencia a favor de H0 (para equilibrar):** el campo tokenizado de Landtoken, con más de USD 850 mil y más de 200 inversiones (declaración comercial, [Bichos de Campo](https://bichosdecampo.com/la-empresa-landtoken-logro-vender-en-apenas-dos-meses-el-primer-campo-tokenizado-en-la-argentina-y-desde-febrero-ofrece-otra-oportunidad-para-pequenos-inversores)). La autorización de tokenización de Illa Belgrano I (E8011). La base minorista masiva (E8004).

---

## 4. Contradicciones detectadas (para A9)

- Financiamiento 2025: USD 33.679 M (CNV vía BAE) frente a USD 32.978 M (BCSF). Para PyMEs: USD 10.480 M frente a 10.212 M.
- RealT: USD 140 M captados (Crypto Briefing) frente a USD 94 M (Outlier).
- Generación Zoe: pérdidas de los 98 denunciantes de USD 170 mil o de más de USD 400 mil, según el pasaje de la misma nota.
- Tamaño global de RWA: USD 22–31 mil M según la métrica.
- iProfesional muestra fecha 2026 en notas de 2019 (E8041). Varias páginas de Blog del Contador e iProfesional tienen fechas de encabezado que no corresponden a la publicación.

## 5. Enlaces rotos o no verificables

- `acionista.com.br` (CVM vs Mercado Bitcoin): 403 en WebFetch.
- PDF de la tesis de UdeSA (repositorio): devolvió HTML y no un PDF.
- Registro CNV de PFC: requiere enviar el formulario de búsqueda. No se ejecutó por protocolo. **Pendiente para A3/A9, por verificación manual.**
- La nota de iProUP sobre tokenización llegó truncada.

## 6. Lo que A8 no pudo establecer (gaps)

- El volumen oficial captado por PFC entre 2017 y 2026 y la cantidad de PFC activas.
- El costo real de estructurar una emisión tokenizada chica en Argentina (sin cotizaciones públicas).
- Sanciones CNV específicas a ofertas tokenizadas no autorizadas en 2025–2026 (no se halló un comunicado específico).
- Tasas 2026 de pagarés en USD y la tasa de default de instrumentos PyME negociados en mercado (no solo bancarios).
