# MANDATO DE INVESTIGACIÓN MULTIAGENTE — MARKETPLACE DE ACTIVOS TOKENIZADOS EN ARGENTINA

**Tipo:** investigación profunda, verificable, orientada a decisión empresarial.
**Fecha base:** 19 de octubre de 2026 (Argentina). Verificar vigencia a la fecha de ejecución.
**Lengua de entregables:** español de Argentina, técnico y preciso.
**Modo de actuación:** autónomo para leer, analizar, organizar y redactar; sin acciones públicas ni financieras.

## 1. Tesis e interrogantes

Hipótesis inicial H0: existe un problema de intermediación/distribución para proyectos productivos tokenizados en Argentina. Una solución tipo marketplace multisectorial podría resolverlo con descubrimiento, estandarización de información, confianza y experiencia simple, utilizando operadores jurídicos/financieros autorizados para las funciones reguladas.

No dar por válida H0. Buscar pruebas a favor y en contra. Reconocer explícitamente si el mercado todavía carece de emisores/inversores suficientes, si la liquidez es impracticable, si el costo de estructuración supera la captación o si el marketplace regulado es inviable para pequeñas empresas.

Preguntas obligatorias:
1. ¿Qué problema existe exactamente y quién está dispuesto a pagar por resolverlo: emisor, inversor, intermediario o estructurador?
2. ¿Cuántas ofertas verificables están activas, cerradas o anunciadas en Argentina? ¿Qué categorías de activos?
3. ¿Qué competidores operan realmente, cuáles solo promocionan tecnología, cuáles tienen transacciones verificables y cuáles se relacionan con CNV?
4. ¿Qué derechos jurídicos adquiere el comprador de cada tipo de token? Comparar acciones, deuda, flujos de ingresos, derechos fiduciarios y tokens de utilidad.
5. ¿Qué actividades necesitan inscripción/registro/autorización en Argentina (PFC, PSAV, intermediación de valores, custodia, negociación secundaria, asesoramiento, promoción)? ¿Qué puede hacer un mero portal informativo?
6. ¿Qué modelo sin tokenización podría resolver el problema con menor costo y riesgo? Medirlo contra el modelo on-chain.
7. ¿Cuál sería el nicho inicial y qué segmento conviene descartar?
8. ¿Cuáles son los puntos de fracaso: fraude, baja calidad de proyectos, liquidez, AML/KYC, conflictos, defaults, gobernanza, disputas y ciberseguridad?
9. ¿Qué evidencias faltan y qué entrevistas/experimentos humanos deben realizarse antes de programar?
10. ¿Qué producto mínimo, qué socios licenciados y qué costos exigiría el lanzamiento legal?

## 2. Modelo organizativo

Crear un agente **orquestador** y estos frentes paralelos (adaptar cantidad real de subagentes disponibles; si no hay subagentes, ejecutar frentes separados y registrar la limitación):

- **A1 Mercado local:** recopilar al menos 12 organizaciones argentinas o explicar por qué no existen tantas realmente comparables. Clasificar marketplace de terceros, emisor propio, tokenizadora, inmobiliaria fraccionada, crowdfunding no-tokenizado, distribución financiera y proveedor de infraestructura. Buscar publicaciones activas y evidencia de transacciones verificables, sin asumir que las cifras de marketing son verificadas. Distinguir presencia en Argentina de licenciamiento argentino.
- **A2 Benchmarks internacionales:** mínimo 10 empresas/modelos, incluidos Republic, Wefunder, Brickken, Reental y referentes latinoamericanos confirmados. Contrastar funciones, oferta, acceso, reputación, monetización, criterios de admisión y tecnología; verificar cada URL oficial. No copiar legislación extranjera a Argentina.
- **A3 Jurídico/regulatorio:** leer normas oficiales y texto vigente a la fecha de investigación: Ley 26.831, Ley 27.349, Ley 27.739, CNV RG 1125/2026, 1150/2026, 1165/2026 y 1172/2026, régimen PSAV vigente, PFC, oferta pública y AML/UIF. Construir una matriz de 8 escenarios (portal informativo, listados con CTA, colocación, emisión propia, custodio, intermediación crypto, exchange secundario, referral a autorizado). Para cada actividad: posible figura, restricciones, autoridad, registro específico, controles, fuentes y grado de certeza. ACLARACIÓN OBLIGATORIA: registro PSAV no equivale por sí solo a autorización de oferta pública de valores negociables. No concluir habilitación operativa sin revisión de abogado especialista argentino y contrastación de registros.
- **A4 Descubrimiento de clientes:** segmentar titulares de pymes, desarrolladores, inversores minoristas, inversores profesionales, ALyC, fiduciarias y plataformas. Preparar entrevistas concretas, muestras y métodos de validación. No simular entrevistas realizadas, testimonios ni demanda.
- **A5 Modelo económico:** explorar monetización por suscripción, publicación, comisión de captación, servicios B2B de compliance, analítica y operación con socios. Estimar unit economics con hipótesis explícitas (GMV, take rate, conversión, CAC, coste legal por emisor, costo KYC por inversor, fraude/default, atención). Construir escenarios conservador/base/optimista, sensibilidad y umbral de rentabilidad. Prohibido presentar como dato real estimaciones sin respaldo.
- **A6 Producto/procesos:** definir journeys de emisor e inversor, onboarding, due diligence, prospecto y riesgos, evaluación, KYC, autorización, campaña, fondos, suscripción, distribución de ingresos, reporting, salida, disputas. Distinguir MVP informativo/comercial del producto financiero regulado. Redactar mapa BPMN conceptual y RACI.
- **A7 Tecnología y arquitectura:** comparar mercado sin blockchain vs registro tokenizado. Proponer stack modular: catálogo, identidad, autorización, verificación documental, scoring, audit trail, controles de transferencia, integraciones con entidad regulada, seguridad, bases de datos, monitoreo, versionado, backoffice. No programar smart contracts de producción ni desplegar infraestructura financiera sin validación jurídica. Evitar blockchain si no demuestra valor incremental.
- **A8 Red team de negocio:** buscar contraejemplos, proyectos fallidos, reclamaciones, problemas de liquidez, riesgo de incumplimiento normativo, costos de captación, dependencia de emisores y riesgos de incentivos. Elaborar razones concretas para **no** emprender esta idea y condiciones que invalidan el proyecto.
- **A9 Auditor de evidencia / QA:** control independiente, deduplicación, resolución de contradicciones, recálculo de tablas, separación hechos/afirmaciones/opiniones, y revisión de citas. Devolver hallazgos no verificados a cada agente.

## 3. Protocolo de investigación

Fase I — Taxonomía y fuentes: escribir glosario corto con crowdfunding, tokenización, emisión, colocación, inversión primaria, mercado secundario, SPV, fideicomiso, securities, PSAV/PFC/ALyC; fuentes regulatorias prioritarias.

Fase II — Exploración paralela: agentes A1 a A8 recolectan información y la vuelcan en archivos separados. Todo número externo necesita URL pública consultable, fecha y ámbito. Registrar evidencia con el contrato `SCHEMA_EVIDENCIA.json` y llevar archivo `evidencia.csv`.

Fase III — Contradicción: A8 intenta falsar H0, A9 audita todos los frentes. No aceptar expresiones como 'lidera el mercado', 'regulado', 'líquido', 'rentabilidad garantizada' o 'mil usuarios' sin prueba verificable.

Fase IV — Síntesis: orquestador elabora alternativas estratégicas y una recomendación basada en evidencia. Dar prioridad a un negocio de distribución/descubrimiento con socios autorizados si reduce exposición operativa; no adoptar la opción preferida sin prueba.

Fase V — Decisión: emitir GO / PILOTO CONDICIONADO / NO-GO, criterios cuantificados y supuestos críticos. Mostrar la evidencia que cambiaría cada conclusión.

## 4. Análisis obligatorio de alternativas

Comparar **cuatro versiones distintas** del negocio:

- M0: directorio/portal de proyectos con información pública verificada, sin recibir órdenes, recomendar inversiones, intermediar ni captar fondos; analizar incluso si su promoción podría ser regulada.
- M1: marketplace de originación comercial y descubrimiento integrado con PFC/ALyC/PSAV u otros terceros autorizados; responsabilidades delineadas en contratos y procesos.
- M2: plataforma integral que gestiona emisiones tokenizadas, KYC, suscripciones, reporting y custodia bajo las autorizaciones/alianzas necesarias.
- M3: mercado secundario con negociación entre inversores; separar requisitos regulatorios, liquidez, manipulación, custodia, liquidación y profundidad de mercado.

Puntuar cada uno 0–5 en: viabilidad regulatoria, velocidad de salida, problema real, oferta disponible, atracción de demanda, CAPEX/OPEX, riesgos operativos, ingresos, escalabilidad y diferenciación. Pesos justificados, sin falsa precisión.

## 5. Entregables y nombres exactos

Guardar en carpeta `research/` y escribir documentos suficientes para permitir auditoría:

1. `00_RESUMEN_EJECUTIVO.md`: máximo 2 páginas, dictamen, oportunidad, competidores clave, barreras, incógnitas y 3 siguientes acciones.
2. `01_MAPA_COMPETITIVO.csv`: empresa;país;URL;categoría;segmento;tokenizada_si_no;rol_regulado_declarado;registro_verificado;estado_ofertas;precio_entrada;modelo_ingresos;prueba_transacciones;fecha_revisión;fuente;confianza. Registrar `No verificable` en campos desconocidos.
3. `02_BENCHMARK_INTERNACIONAL.md`: 10 modelos con ventajas/limitaciones transferibles a Argentina.
4. `03_DICTAMEN_REGULATORIO_PRELIMINAR.md`: matriz de escenarios y requisitos legales, con citas a artículos; marcar 'hipótesis para abogado' cuando corresponda. No sustituye asesoramiento jurídico.
5. `04_MAPA_DE_PROCESOS.md`: pasos, responsabilidades y documentos, desde alta de emisor hasta pago/reporting y salida.
6. `05_MODELOS_DE_NEGOCIO.xlsx` **o** `.csv`: escenarios y fórmula visible de ingresos = colocaciones × ticket promedio × comisión, con costos y sensibilidades. Si se usa Excel, fórmulas editables.
7. `06_MVP_Y_ARQUITECTURA.md`: tres versiones sucesivas de MVP, tecnología requerida, seguridad y controles.
8. `07_PLAN_DE_VALIDACION.md`: selección del nicho, plan de 15 a 20 entrevistas **pendientes**, preguntas no inductivas, landing de prueba sin captación de dinero, métricas de disposición a pagar, hitos 30/60/90 días.
9. `08_RIESGOS_Y_KILL_CRITERIA.md`: riesgos, mitigaciones y criterios concretos para abandonar idea.
10. `09_EVIDENCIAS.csv`: id;claim;url;publisher;published_at;accessed_at;type;confidence;notes;confirmation_status.
11. `10_DECISION.md`: GO / PILOTO CONDICIONADO / NO-GO y priorización de tres modelos.
12. `11_PREGUNTAS_PARA_ABOGADO_Y_OPERADORES.md`: no menos de 15 preguntas, organizadas por función operativa.
13. `12_LOG_EJECUCION.md`: fecha de ejecución, agentes ejecutados, bloqueos, tareas completadas, tareas incompletas, advertencias de costos, enlaces rotos y próximos pasos.

## 6. Criterios de aceptación

- Fuentes oficiales para todos los hechos regulatorios; documentos actuales cotejados con cambios en octubre de 2026.
- No confundir una empresa que declara operar con una empresa cuyos productos/registros estén comprobados.
- No confundir oferta de inversión, crowdfunding y tokenización. Clarificar que un token no crea derechos legales por sí mismo.
- Incluye actores argentinos **y** comparadores internacionales, con enlace directo a oferta y al funcionamiento.
- No afirmar demanda, ROI, tamaño de mercado, liquidez, beneficios ni habilitaciones sin fuente.
- Indicar nivel de incertidumbre y dependencias críticas.
- Resultados trazables a URLs, no bibliografías inventadas.
- Al menos un razonamiento sólido por el que la idea puede fracasar.
- Establecer un plan de validación más barato que construir un sistema financiero completo.
- Recomendar decisión con fecha, condiciones y responsable humano para validación legal.

## 7. Autonomía y límites

PODÉS: buscar, leer fuentes abiertas, comparar, producir archivos privados, hacer cálculos, detectar contradicciones, generar checklists y planes.

NO PODÉS: invertir, ofrecer tokens, custodiar activos, enviar mensajes o solicitudes a terceros, registrar empresas o cuentas, publicar publicidad financiera, tomar decisiones jurídicas vinculantes, entrar a banca/billeteras, emitir activos, hacer deploy, comprometer gasto en servicios o ejecutar cambios permanentes sin consentimiento expreso.

Si se agota el presupuesto/capacidad de ejecución, priorizar: **matriz regulatoria verificada → competencia local real → entrevistas/validación → modelo económico → arquitectura**. Entregar resultados parciales con trazabilidad y lista de pendientes; nunca ocultar fallas.

## 8. Instrucción final al orquestador

No persigas producir un informe impresionante: perseguí una decisión empresarial correcta. Tu trabajo concluye cuando pueda responderse con rigor: **¿Existe una oportunidad defendible de marketplace de financiación de proyectos productivos tokenizados en Argentina, para quién, bajo qué estructura, a qué costo, con qué competidores, y qué necesitamos demostrar antes de gastar en desarrollo?**
