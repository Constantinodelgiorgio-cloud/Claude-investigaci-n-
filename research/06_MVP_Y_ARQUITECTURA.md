# 06 — MVP y arquitectura (A7)

**Fecha:** 2026-10-19 · **Base:** `frentes/A7_tecnologia.md` (comparativa y stack detallado), `03_DICTAMEN_REGULATORIO_PRELIMINAR.md`, `05_MODELOS_DE_NEGOCIO.xlsx`.
**Límites:** no hay código de smart contracts ni despliegue de infraestructura financiera. Nada de esto se construye antes de que los kill criteria K1–K8 de `08` estén en verde (gasto hasta el día 90 = solo validación).

## 1. Decisión tecnológica central

**Primero, sin blockchain.** Según el régimen CNV de tokenización (Tít. XXII, RG 1069/2025 y RG 1150/2026), el valor negociable sigue depositado en un ADCVN y el token es una "forma de representación adicional" que "no implicará la creación de un nuevo valor negociable" (Tít. XXII art. 7, E3019/E5029). Además:
- solo circula entre hasta 5 PSAV designados;
- está prohibido usarlo en DeFi;
- exige doble conciliación;
- el sandbox vence el 31/12/2027.

En esas condiciones, la blockchain **no le agrega valor suficiente** a un marketplace de descubrimiento y originación (inferencia A7, certeza media). El único beneficio material es **comercial**: llegar a la base de clientes de PSAV y exchanges que ya distribuyen RWA (por ejemplo, Ripio con el FF Landtoken I). Ese beneficio se obtiene **integrándose con el socio que tokeniza**, sin operar tokens propios.

La "verificabilidad" se consigue con un audit trail append-only y anclaje diario de un hash raíz en una cadena pública o en la BFA (opción D de A7). Cuesta muy poco y no tiene implicancias regulatorias de custodia.

## 2. Tres versiones sucesivas de MVP

| | **MVP-0 (M0): portal informativo verificado** | **MVP-1 (M1): originación + derivación a autorizado** | **MVP-2 (M2-light): tokenización vía socio** |
|---|---|---|---|
| Objetivo de aprendizaje | ¿Hay emisores dispuestos a entregar información y operadores interesados en recibirla? | ¿Un operador autorizado coloca un proyecto originado por nosotros? ¿Alguien paga? | ¿El canal PSAV aporta inversores a menor CAC que el canal ALyC? |
| Condición de entrada | Dictamen del abogado sobre el escenario 1 de `03` | K1, K2, K4 y K7 en verde (`08`) | K9 en verde (primera colocación) y demanda probada en el canal cripto |
| Funciones | Catálogo de fichas de **ofertas ya autorizadas** (información pública, con enlace al agente o PFC), formulario de pre-calificación de emisores, contenido educativo | Workflow de DD, KYB de emisores, data room, scoring explicable (no calificación de riesgo), integración API/SFTP con 1–2 socios, reglas de elegibilidad en UVA | Adaptador a un PSAV/tokenizador (ERC-3643 u otro, **operado por el socio**), conciliación diaria token ↔ ADCVN ↔ BD |
| Qué **no** hace | Sin CTA "Invertir", sin rendimientos destacados, sin ranking, sin fondos ni órdenes | Sin recibir fondos ni órdenes; el KYC formal del inversor lo hace el socio | Sin custodiar llaves ni fondos, sin smart contracts propios, sin secundario |
| Módulos (A7 §4) | 1, 3, 4, 6, 9, 10, 12, 13 (mínimos) | + 2, 5, 7a, 8, 11; anclaje opcional en 6 | + 7b |
| Tecnología | Sitio SSR + CMS headless, PostgreSQL gestionado, almacenamiento con versionado, backoffice low-code | + proveedor KYB/KYC (Sumsub/Veriff/RENAPER vía intermediario), motor de workflow, webhooks | + API del tokenizador |
| Costo de infraestructura (SUPUESTO) | < USD 1.000/mes | USD 2–5k/mes | + licencia del socio (referencia Brickken €3–9k/año, E5007) |
| Equipo mínimo (SUPUESTO) | 1 producto/dev + 1 analista de DD a tiempo parcial | + 1 compliance, + 1 comercial B2B | + integración técnica con el socio |

## 3. Arquitectura lógica (agnóstica de blockchain)

```
            ┌──────────── Backoffice (compliance, DD, comité, reclamos) ───────────┐
            │                                                                       │
Emisor ──► Onboarding/KYB ──► Workflow (máquina de estados, 4 ojos) ──► Catálogo de fichas versionadas ──► Inversor (lectura)
            │                     │                                         │
            │                Verificación documental (hash SHA-256)        Link a operador autorizado
            │                     │                                         │
            └──────────────► Audit trail append-only (WORM) ──► anclaje diario del hash raíz (cadena pública/BFA)
                                  │
                         Integraciones con socios regulados (API/SFTP): leads, estado de colocación, pagos, reportes
                                  │
                         [opcional MVP-2] Adaptador de tokenización del socio (sin llaves propias)
```

## 4. Seguridad y controles

| Control | Implementación | Por qué |
|---|---|---|
| Separación de funciones | La publicación de una ficha exige dos aprobadores distintos; el comercial no aprueba DD | Conflicto de interés entre comisión y calidad (A8) |
| Minimización de datos personales | Si el socio hace KYC, guardar solo la referencia y el resultado; registro de accesos a datos KYC | Ley 25.326; reduce el impacto de una brecha |
| Cifrado y secretos | TLS, cifrado en reposo con KMS, gestor de secretos, MFA obligatorio, RBAC | Base mínima |
| Integridad documental | Hash de cada documento en el audit trail; versión y fecha visibles en cada ficha | Poder reconstruir qué vio un inversor en la fecha X (disputas) |
| Reglas de publicidad | Plantillas con leyendas fijas; bloqueo de palabras ("garantizado", "sin riesgo", "líquido") en el CMS | Ley 26.831 arts. 112–116; RG 1172 arts. 33–34 |
| Elegibilidad | Topes en UVA actualizados a diario (API BCRA), calculados **antes** de derivar; la decisión final es del socio | RG 942/2022 y RG 1125/2026 |
| AML | Señales de alerta (múltiples cuentas, emisores con BF ocultos) que se escalan al sujeto obligado; definir por contrato quién reporta a la UIF | Res. UIF 78/2023 y 49/2024 |
| Continuidad | Backups cifrados, PITR, staging sin datos reales, pentest antes de MVP-1 | Ciberseguridad (riesgo en `08`) |
| Tokenización (solo MVP-2) | Estándar *Final* (ERC-3643) operado por el socio, con pausa, congelamiento y recuperación; conciliación diaria con alertas; sin oráculos para pagos | Divergencia de registros y riesgo de llaves (A7 §3) |

## 5. Lo que no se construye (explícito)

- Smart contracts propios, custodia de llaves, fondos o stablecoins.
- Mercado secundario (M3), conexión a DeFi (prohibida por Tít. XXII art. 5 f) y oráculos que disparen pagos.
- Scoring con ML opaco o cualquier cosa que pueda confundirse con una calificación de riesgo regulada.

## 6. Comparativa resumida: sin blockchain vs. tokenizado (detalle en A7 §3)

| Dimensión | Sin blockchain | Tokenizado (AR, hoy) |
|---|---|---|
| Registro legal | ADCVN / agente de registro / libro de la PFC | El mismo, más un espejo on-chain |
| Costo y operación | Bajo | Más alto: PSAV, conciliación, custodia de llaves por el socio |
| Liquidez | Depende de compradores | Igual; solo entre ≤5 PSAV y sin DeFi |
| Auditoría | Audit trail + anclaje de hash | Ledger compartido (poco incremental frente al anclaje) |
| Distribución | Canal ALyC/PFC | **+ canal PSAV** (único beneficio material) |
| Riesgo regulatorio | Estable | Sandbox hasta 31/12/2027 |
