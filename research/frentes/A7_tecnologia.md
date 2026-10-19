# A7 — Tecnología y arquitectura: registro centralizado vs. registro tokenizado

**Frente:** A7 · **Fecha:** 2026-10-19 · **Evidencia:** `A5A7_evidencia.csv` (E5029–E5042)
**Alcance:** comparar arquitecturas y proponer un stack modular. **No incluye código de smart contracts** ni despliegue (Mandato §7). Nada de esto valida jurídicamente una estructura; el rol de cada actor regulado lo tiene que confirmar A3 con un abogado.

---

## 1. Punto de partida regulatorio que condiciona la arquitectura (DATO)

En el régimen argentino de tokenización de la CNV (RG 1069/2025, ampliada por RG 1081 y 1087/2025 y RG 1150/2026):

- **El token no es el registro primario.** Los valores negociables se emiten primero en forma «tradicional» (cartular o escritural) y se depositan en un **ADCVN** (Caja de Valores), en una cuenta individualizada a nombre de uno o más **titulares registrales** (PSAV o agente de PIC) que actúan por cuenta de los inversores. La representación digital es una **«forma de representación adicional»** y no un valor nuevo (RG 1069, art. 5 inc. a–b y art. 7). [E5029]
- **Los tokens deben ser permisionados.** No pueden transferirse ni negociarse fuera de los PSAV intervinientes (máximo 5) ni en protocolos descentralizados. Deben generarse «bajo redes o contratos inteligentes que impidan transferencias no permitidas» (art. 5 inc. f). [E5029]
- **Divulgación técnica obligatoria.** El documento de emisión tiene que indicar el tipo de red (pública, privada o permisionada), el consenso, el lenguaje y los estándares de los contratos inteligentes y las medidas de ciberseguridad. También tiene que definir quién responde por la «entidad especializada en TRD» (art. 22). [E5029]
- **Interoperabilidad y conciliación en tiempo real entre PSAV.** Los PSAV responden por cualquier divergencia con los valores depositados en el ADCVN. [E5029]
- **Custodia de llaves por PSAV (RG 1172/2026).** Exige describir la arquitectura de billeteras (frías, tibias, calientes), las redes usadas, multifirma, distribución geográfica de llaves y segregación de activos de clientes. [E5030]
- **Sandbox vigente hasta el 31/12/2027 (RG 1150/2026).** [E5032]

**Consecuencia de diseño (inferencia):** en Argentina la cadena funciona hoy como **espejo sincronizado** de un registro legal que sigue estando en la Caja de Valores. Una prensa especializada recoge la crítica de que los tokens serían «simples espejos» de títulos depositados [E5031]. Esto reduce mucho el valor incremental de la blockchain para un marketplace: el registro legal, la custodia y la liquidación siguen pasando por infraestructura tradicional, y encima hay que operar y conciliar una segunda capa.

---

## 2. Opciones de arquitectura

| Opción | Registro de titularidad legal | Rol de la plataforma | Quién opera lo regulado |
|---|---|---|---|
| **A. Sin blockchain (centralizado)** | ADCVN o agente de registro del emisor, o el libro de la PFC o del fiduciario | Catálogo, originación, KYC delegado, flujo documental, reporting | PFC / ALyC / fiduciario aliado (M0–M1) |
| **B. Tokenizado permisionado sobre red pública EVM** (ERC-3643 o similar) | ADCVN (legal) + espejo en cadena pública (L2 o sidechain) | Igual que A + integración con un PSAV titular registral y conciliación | PSAV registrado + ADCVN + fiduciario |
| **C. Tokenizado sobre red privada o consorcio** (p. ej. Besu, Fabric) | ADCVN (legal) + espejo en red privada | Igual que B, con más operación propia | Ídem B, y además el operador de la red |
| **D. Híbrido «anclaje»** | Registro centralizado (A) + hash periódico del audit trail en una cadena pública | Igual que A + prueba de integridad | Igual que A |

Notas de referencia:
- **ERC-3643 (T-REX)** es un estándar *Final* del proceso EIP (creado el 09/07/2021). Combina un token compatible con ERC-20 con un Identity Registry (wallet → identidad on-chain → país), un módulo de Compliance (`canTransfer`), Trusted Issuers y Claim Topics. Permite congelar wallets total o parcialmente, pausar, hacer transferencias forzadas y recuperar tokens de una wallet perdida. Encaja en lo técnico con el art. 5 inc. f de la RG 1069. [E5033]
- **ERC-1400** sigue en estado *Draft*. Es un paraguas de ERC-1410, 1594, 1643 y 1644 (particiones, documentos, operaciones de controlador). Su impulsor, Polymath, migró a una cadena propia. [E5034]
- **Tokeny** documenta ERC-3643 para redes EVM públicas o privadas, sin lista de redes en la página consultada. [E5035] **Securitize** opera con entidades registradas en EE. UU. (transfer agent, broker-dealer, ATS) y su DS Protocol corre, según fuentes secundarias, en Avalanche y Solana, entre otras. [E5036] **Brickken** ofrece «multichain» por plan (1 red incluida en Core, 3 en Advanced, todas en Professional) y «redes privadas o L1 dedicadas» en Enterprise. [E5007]
- **Qué red usan las tokenizaciones argentinas conocidas:** la del primer FF tokenizado con oferta pública (Landtoken I: Allaria Fiduciaria como fiduciario, Justoken / Tech Demeter S.A. como entidad generadora, distribución por ALyC y por Ripio) **no aparece publicada en ninguna fuente consultada** (no verificable; está en el prospecto CNV, que no se leyó). [E5037, E5038] Justoken anuncia un proyecto con YPF Luz sobre **XRP Ledger** (declaración comercial, mar-2026). [E5039] **No hay información pública sobre una «red del sandbox CNV»**: la norma no fija una red, solo obliga a divulgarla (art. 5).

---

## 3. Valor incremental de la blockchain: evaluación por dimensión

Escala: **+** aporta, **0** neutro, **−** resta. Valoraciones de A7 (inferencia), con la evidencia citada cuando existe.

| Dimensión | A. Centralizado | B/C. Tokenizado | Valor incremental de B/C en Argentina | Comentario |
|---|---|---|---|---|
| **Costo de puesta en marcha** | Bajo: SaaS + BD + integraciones | Medio a alto: SaaS de tokenización €3k–9k/año en Brickken + auditoría de contratos + PSAV + conciliación con ADCVN | **−** | La licencia SaaS es barata (E5007). Lo caro es la operación regulada (PSAV con tasa CNV de ARS 13,36 M/año para persona jurídica, E5013) y la doble conciliación |
| **Costo por transacción** | ~0 marginal | Gas en L2: centavos de USD; en Ethereum mainnet ≈USD 1–5 [E5040] | **0** | Irrelevante frente a la comisión, salvo en mainnet |
| **Costo de cumplimiento** | KYC/AML por entidad regulada | Igual + identidad on-chain + responsable de la entidad TRD (art. 22) + reglas de custodia de llaves (RG 1172) | **−** | Se suman capas de control; ninguna se elimina |
| **Transferencias / liquidez secundaria** | Transferencia vía ALyC/ADCVN o cesión contractual | Transferencia entre PSAV intervinientes (≤5). Prohibido DeFi | **0 / +** marginal | La liquidez depende de que haya compradores, no de la tecnología. La norma cierra la composabilidad abierta |
| **Interoperabilidad** | APIs bilaterales | Estándar común entre PSAV designados (exigido) | **+** limitado | Solo dentro de un conjunto cerrado de PSAV. No hay interoperabilidad global |
| **Fraccionamiento / ticket mínimo** | Posible con cuotapartes / VN bajo (ADCVN) | Nativo | **0 / +** | En FF tradicional ya se pueden emitir VN bajos. El tope lo fija la regulación (UVA), no la tecnología |
| **Auditoría / trazabilidad** | Audit trail append-only firmado (WORM) + auditor externo | Ledger compartido verificable por terceros | **+** moderado | Se replica en buena medida con la opción D (anclaje de hashes) a costo mínimo |
| **Distribución de flujos (cupones/dividendos)** | Agente de pago / ADCVN | Distribución programática (stablecoin o fiat vía PSAV) | **+** potencial | Hoy depende de la conversión fiat↔stablecoin y de la regulación cambiaria. Sin evidencia de ahorro en Argentina |
| **Acceso a canal cripto** (exchanges/PSAV con base de usuarios) | No | Sí: p. ej. Ripio como canal del FF Landtoken [E5037] | **+** relevante | Es el argumento comercial más fuerte: un **canal de distribución** con inversores ya con KYC hecho |
| **Marketing / percepción** | Neutral | «Tokenizado» atrae atención | **+ / −** | Riesgo de que el término confunda sobre derechos y liquidez (Mandato §6) |
| **Riesgo de llaves privadas** | No aplica | Pérdida o robo; requiere MPC/multifirma y procedimientos (RG 1172) | **−** | Robos en cripto 2025 ≈USD 3,4 mil M, concentrados en fallas operativas (Bybit USD 1,4 mil M) [E5041] |
| **Riesgo de bugs en smart contracts** | No aplica | Explotaciones; mitigación con auditoría, estándar probado, pausa y recuperación | **−** | ERC-3643 trae pausa, congelamiento y recuperación (E5033), pero eso significa que el emisor o agente conserva control centralizado |
| **Riesgo de oráculos** | No aplica | Si los pagos dependen de datos externos (precio, cobranzas) | **−** | Mitigar con agente de cálculo humano. No automatizar pagos con oráculos en el MVP |
| **Riesgo de divergencia de registros** | Un solo registro | Dos registros (ADCVN y cadena); los PSAV responden por las divergencias [E5029] | **−** | Riesgo operativo nuevo y específico de la arquitectura argentina |
| **Riesgo regulatorio / de cambio de norma** | Estable | Sandbox hasta 31/12/2027 [E5032]. 5 RG de tokenización/PSAV entre jun-2025 y oct-2026, 16 meses (1069→1081→1087→1150, más 1172) | **−** | Diseñar para salir del sandbox o migrar sin rehacer el core |
| **Riesgo de la red** (congestión, fork, cese de la L2) | No aplica | Real en L2 y sidechains | **−** | Hace falta poder migrar el token (ERC-3643 permite reemitir a otra red, pero con costo) |

**Conclusión A7 (inferencia, certeza media):** para un marketplace de **descubrimiento y originación (M0–M1)**, la blockchain **no aporta valor incremental suficiente** frente a un registro centralizado con audit trail sellado (opción A+D). El único beneficio material es **comercial**: acceder a la base de usuarios de PSAV o exchanges que ya distribuyen productos tokenizados. Ese acceso se consigue **integrándose como originador con un PSAV y una fiduciaria que tokenizan**, sin que la plataforma opere tokens propios. La tokenización propia (M2) solo se justificaría si: (i) un PSAV y una fiduciaria aliados absorben la operación regulada, (ii) hay demanda probada en el canal cripto (prueba que hoy no existe, ver A4) y (iii) el costo fijo de la doble conciliación se reparte entre muchas emisiones.

---

## 4. Stack modular propuesto (agnóstico de blockchain)

Principio: **el core no depende de la cadena**. La tokenización queda como un adaptador opcional (módulo 7b) que opera un tercero regulado. Así M0 y M1 se lanzan sin blockchain, y M2 se suma después sin reescribir nada.

| # | Módulo | Función | Tecnología sugerida (no vinculante) | Build / Buy | Controles clave |
|---|---|---|---|---|---|
| 1 | **Catálogo de proyectos** | Ficha estandarizada: emisor, instrumento, derechos, riesgos, documentos, estado (anunciado/activo/cerrado), regulador y vehículo | Next.js/SSR + CMS headless; esquema JSON versionado por ficha | Build | Ninguna ficha se publica sin aprobación del módulo 3. Leyendas regulatorias fijas. Sin CTA de inversión en M0 |
| 2 | **Identidad (KYC/KYB)** | Alta de inversor y emisor, validación DNI/RENAPER, prueba de vida, PEP/sanciones, KYB societario | Proveedor externo (Sumsub, Veriff, MetaMap o Didit) vía API + RENAPER por convenio o intermediario | Buy | Si el KYC lo hace la entidad regulada aliada, la plataforma **no duplica datos**: guarda el token o referencia y el resultado |
| 3 | **Autorización y workflow** | Máquina de estados de proyecto y campaña (borrador → DD → comité → publicado → cerrado), aprobación en dos pasos, segregación de funciones | Motor de workflow (Temporal o Camunda) o máquina de estados en el backend | Build sobre OSS | 4 ojos en publicación. Registro de quién aprobó qué y cuándo |
| 4 | **Verificación documental** | Recepción, OCR, verificación de autenticidad (estatutos, balances, AFIP/ARCA, CNV), checklist DD | Almacenamiento de objetos con versionado + OCR + verificaciones manuales | Buy (OCR) + Build | Hash SHA-256 de cada documento en el audit trail. Retención según UIF/CNV |
| 5 | **Scoring / evaluación** | Matriz de riesgo del proyecto (no recomendación de inversión): completitud, antecedentes, garantías, concentración | Reglas versionadas + revisión humana. Nada de ML opaco en el MVP | Build | Modelo versionado y explicable. Sin «calificación» que pueda confundirse con calificación de riesgo regulada (A3) |
| 6 | **Audit trail** | Log inmutable de eventos (alta, cambios de ficha, aprobaciones, accesos, consentimientos) | Tabla append-only + WORM (p. ej. S3 Object Lock) + **anclaje diario del hash raíz (Merkle) en una cadena pública o en BFA** (opción D) | Build | Esto da la «verificabilidad» sin tokenizar. El Boletín Oficial ofrece autenticaciones y recibos sellados en BFA (Blockchain Federal Argentina) [E5042] |
| 7a | **Controles de transferencia (sin token)** | Reglas de elegibilidad (topes UVA por inversor, 20% de ingresos, calificado o no, mínimo de 5 inversores) evaluadas **antes** de derivar al socio | Motor de reglas parametrizado en UVA con actualización diaria desde la API BCRA | Build | Los topes de RG 942 y RG 1125 (E5009–E5011) se validan, pero **la decisión final es de la entidad regulada** |
| 7b | **Adaptador de tokenización (opcional, M2)** | Integración con un PSAV o tokenizador que emite y opera tokens permisionados (ERC-3643 o equivalente) y concilia con el ADCVN | API del proveedor (Brickken, Tokeny, Justoken u otro). La plataforma **no tiene llaves** | Buy / socio | Conciliación diaria token ↔ ADCVN ↔ BD. Alerta ante divergencias |
| 8 | **Integraciones con entidades reguladas** | PFC, ALyC, fiduciaria, PSAV, ADCVN: derivación de leads, estado de órdenes, resultados de colocación, pagos | API REST/webhooks + SFTP de respaldo. Contratos de datos versionados | Build | **La plataforma no recibe fondos.** Toda orden y todo pago van por la entidad regulada (M1) |
| 9 | **Seguridad** | IAM con MFA y RBAC, cifrado en reposo y en tránsito, gestión de secretos, WAF, pentest anual, gestión de vulnerabilidades | Cloud con KMS + SSO + WAF + escáneres en CI | Buy + config | Datos personales bajo Ley 25.326 y su reforma. Mínimo privilegio. Registro de accesos a datos KYC |
| 10 | **Bases de datos** | Transaccional (proyectos, usuarios, estados), documental, analítica | PostgreSQL (con RLS) + almacenamiento de objetos + data warehouse aparte | Buy (gestionado) | Backups cifrados, PITR, ambiente de staging sin datos reales |
| 11 | **Monitoreo** | Técnico (APM, logs, alertas) y de negocio/AML (patrones de alta, múltiples cuentas, fraude de emisor) | Observabilidad gestionada + reglas AML del proveedor KYC | Buy | Reporte de operación sospechosa vía la entidad obligada (UIF). Definir quién es sujeto obligado |
| 12 | **Versionado** | Versiones de fichas, documentos, términos, reglas de scoring y topes regulatorios | Git para código y reglas, versionado de objetos, `effective_from` en tablas de parámetros | Build | Toda ficha publicada muestra la versión y la fecha. Se puede reconstruir qué vio un inversor en la fecha X |
| 13 | **Backoffice** | Consola de compliance, DD, comité, atención, reclamos y disputas, reporting a socios | Admin interno (Retool o similar en MVP) | Buy → Build | Acciones sensibles con doble aprobación. Exportes para auditor |

### Secuencia por versión de MVP (alineada con M0/M1/M2)

- **MVP-0 (M0, portal informativo):** módulos 1, 3, 4, 6 (sin anclaje), 9, 10, 12 y 13 en versión mínima. Sin KYC de inversores ni órdenes. Costo de infraestructura bajo (estimación A7, SUPUESTO: < USD 1.000/mes en cloud y SaaS).
- **MVP-1 (M1, originación + derivación a regulado):** suma 2 (KYB del emisor, y KYC del inversor solo si el socio lo delega), 5, 7a, 8 y 11. Anclaje opcional del audit trail (D).
- **MVP-2 (M2, solo si se validan las condiciones de §3):** suma el adaptador 7b con un PSAV o tokenizador aliado. La plataforma sigue sin custodiar llaves ni fondos.

### Decisiones explícitas de no hacer (MVP)

- No desarrollar ni desplegar smart contracts propios. Si se tokeniza, usar un estándar *Final* (ERC-3643) operado por el tokenizador o PSAV regulado.
- No custodiar llaves privadas, fondos ni stablecoins.
- No usar oráculos para disparar pagos.
- No ofrecer mercado secundario (M3) ni conexión a DeFi (prohibido por RG 1069 art. 5 f).

---

## 5. Preguntas técnicas para operadores (entrada para `11_PREGUNTAS...`)

1. ¿Qué red y qué estándar de token usó el FF Landtoken I y qué costo de operación anual tiene la entidad TRD? (Leer prospecto CNV / preguntar a Justoken y Allaria.)
2. ¿Cómo se concilian en la práctica ADCVN y la cadena? ¿Con qué frecuencia y quién firma la conciliación?
3. ¿Un PSAV titular registral acepta lotes chicos (USD 0,2–2 M) o tiene un mínimo económico?
4. ¿La CNV exige auditoría externa de smart contracts? La norma pide divulgar estándares y ciberseguridad, pero el texto leído no menciona auditoría (A3 debe verificarlo).
5. ¿La entidad regulada aliada acepta KYC hecho por un proveedor de la plataforma (reliance) o lo repite?

## 6. Limitaciones y enlaces

- RG 1069 se leyó en su texto original del BO (13/06/2025). Las modificaciones posteriores (1081, 1087, 1150) se conocen solo por comunicados o prensa. A3 tiene que verificar el texto ordenado vigente.
- No se pudo leer el prospecto del FF Landtoken I. La red usada queda **no verificable**.
- Artículo de abogados.com.ar truncado en WebFetch (se leyó parcialmente).
- Fuentes de Securitize, Brickken (redes) y costos de gas: secundarias o agregadores, certeza baja a media.
