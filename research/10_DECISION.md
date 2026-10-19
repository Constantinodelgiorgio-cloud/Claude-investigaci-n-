# 10 — Decisión

**Fecha de la decisión:** 2026-10-19 · **Próxima revisión obligatoria:** 2027-01-17 (día 90) · **Responsable humano de la validación legal:** *a designar por el promotor* (abogado argentino especialista en mercado de capitales y PLA/FT). **Responsable de negocio:** *a designar*.
**Advertencia:** ninguna entrevista se hizo todavía. Los supuestos económicos no están validados (`05`). El encuadre regulatorio es preliminar (`03`).

## Dictamen

| Alternativa | Dictamen |
|---|---|
| **Marketplace tokenizado, multisectorial y minorista (H0 tal como está formulada)** | **NO-GO** |
| **M3 — mercado secundario** | **NO-GO** |
| **M2 — plataforma integral (emisión tokenizada, KYC, suscripción, custodia)** | **NO-GO por ahora.** Se reevalúa recién después de una colocación piloto exitosa vía socio |
| **M1 — originación y preparación de emisores pyme para operadores autorizados, sin tokenización propia y en un nicho vertical** | **PILOTO CONDICIONADO**, solo de validación (90 días, sin desarrollo de software financiero) |
| **M0 — portal informativo** | Se usa **como herramienta de validación** de M1 (landing y fichas de ofertas ya autorizadas), no como negocio autónomo |

## Por qué (evidencia resumida)

1. **El problema de distribución no está demostrado; el de originación, quizá sí.**
   - Las pymes ya consiguieron USD 10.480 M en el mercado de capitales en 2025 sin tokenizar, 66% en pagarés (CNV, informe anual, E5024/E8001).
   - Hay 12,3 M de cuentas comitentes (A8).
   - El cuello de botella plausible es conseguir emisores chicos con calidad crediticia y documentación suficiente, no llegar a los inversores. *Hipótesis a validar (K1, K8).*
2. **La oferta local tokenizada es chica y casi toda inmobiliaria.**
   - De 18 organizaciones relevadas, unas 6 son comparables (A1).
   - Solo hay 3 emisiones con oferta pública CNV y representación digital identificadas, todas fideicomisos financieros (Landtoken I, Illa Belgrano I, Espacio Añelo). Las resoluciones están citadas por terceros y falta cotejarlas en la AIF.
   - El actor no tokenizado con más volumen declarado (Crowdium, USD 13,8 M en 18 proyectos, cifra propia) **no necesitó token**.
3. **El token no agrega derechos ni liquidez.**
   - La representación digital "no implicará la creación de un nuevo valor negociable" (Tít. XXII art. 7, E3019).
   - Circula solo entre hasta 5 PSAV, sin DeFi, y el sandbox vence el 31/12/2027 (RG 1150).
   - Afuera, RealT anunció su liquidación en jul-2026 y la negociación secundaria de RWA es mínima (A2, A8).
4. **El registro PSAV no habilita oferta pública de valores negociables** (RG 1172/2026, art. 38, E3024). Varios actores locales lo usan como sello de confianza (A1). Es un riesgo reputacional para todo el segmento y un argumento contra competir en ese terreno.
5. **La economía minorista no cierra con los supuestos base** (`05`, hoja Modelo_M2):
   - Con ticket de USD 800, 2 suscripciones por inversor y CAC de USD 267, el margen de contribución es **negativo** (−12% del GMV): crecer agranda la pérdida.
   - M2 solo cierra en el escenario optimista: CAC ≤ USD 50 y ticket ≥ USD 2.000.
   - Además, la RG 1125 limita al minorista a UVA 3.000 por emisión (≈USD 4.300) y la PFC a UVA 1,5 M por proyecto (≈USD 2,1 M).
6. **M1 tiene contribución positiva en el escenario base, pero es chica:**
   - unos USD 6.500 por campaña;
   - el equilibrio está en unas 23 campañas por año con fee de originación del 2,5% y monto medio de USD 400k (`05`, Modelo_M1);
   - mejora mucho con montos ≥ USD 1 M (Sensibilidad, tabla 4).
   - Su legalidad (fee por éxito pagado por una ALyC o PFC a un originador no registrado, o la necesidad de registrarse como AP/AAGI) es **hipótesis para abogado** (`03` esc. 2 y 8; `11`).
7. **Contra el proyecto pesan:**
   - Hay alternativas no tokenizadas más baratas: cheques y pagarés avalados por SGR en el MAV, ON pyme y FF pyme con arancel CNV del 0,015% (E5012).
   - Los costos fijos de estructuración son altos en emisiones chicas: es una inferencia, a medir en K3.
   - Hubo fraudes recientes (Generación Zoe, $LIBRA) y desconfianza en fideicomisos inmobiliarios.

## Puntuación de los cuatro modelos (0–5; ponderada a 100)

Pesos justificados:
- **Viabilidad regulatoria 20%:** es la restricción binaria del mandato.
- **Problema real 15%:** la tesis central está en duda.
- **Oferta, demanda, velocidad, CAPEX/OPEX y riesgos operativos, 10% cada uno.**
- **Ingresos, escalabilidad y diferenciación, 5% cada uno:** todavía no hay datos para distinguirlos con precisión.

Las puntuaciones son juicios del orquestador sobre la evidencia citada, no mediciones. Una diferencia menor a unos 5 puntos debe leerse como empate.

| Criterio (peso) | M0 portal | M1 originación + socios | M2 integral | M3 secundario |
|---|---|---|---|---|
| Viabilidad regulatoria (20) | 3: sin registro *si* no hay invitación a operar (`03` esc. 1), certeza media/baja | 3: hay figuras (referenciador art. 35 RG 1172, AP, AAGI), falta dictamen | 1: varias licencias incompatibles entre sí (PFC no puede tener otras categorías; agente no puede ser PSAV) | 1: muy restringido (solo secundario propio de la PFC, ≤5 PSAV, mercado/ACVN) |
| Velocidad de salida (10) | 5 | 3 | 1 | 0 |
| Problema real (15) | 2 | 3: posible dolor de originación para operadores (por validar) | 2 | 1: no hay volumen secundario verificable |
| Oferta disponible (10) | 2: pocas ofertas comparables | 3: hay pymes que ya emiten (USD 10.480 M) | 2 | 1 |
| Atracción de demanda (10) | 2 | 3: la demanda la pone el socio | 2: CAC minorista sin benchmark, el modelo no cierra en base | 1 |
| CAPEX/OPEX (10) | 5 | 4 | 1: PN y tasas de varias licencias, conciliación | 1 |
| Riesgos operativos (10, 5 = bajo) | 4 | 3 | 1: custodia, llaves, fraude, AML | 1 |
| Ingresos (5) | 1: sin fuente de ingreso lícita clara sin riesgo | 2: equilibrio ≈23 campañas por año | 2 | 1 |
| Escalabilidad (5) | 2 | 3 | 3 | 2 |
| Diferenciación (5) | 2 | 3 | 2: Volsmart, Efaysto, Metro Futuro y Justoken ya ocupan el espacio | 2 |
| **Total ponderado (/100)** | **59** | **61** | **31** | **20** |

**Lectura:** M0 y M1 quedan prácticamente empatados en puntaje. M1 se prioriza porque es el único con una fuente de ingreso plausible. M0 se usa como su primer paso, barato y de bajo riesgo.

**Priorización:**
1. **M1** en un nicho vertical (agroindustria o energía distribuida, a elegir con entrevistas: `07`).
2. **M0** como instrumento de validación.
3. **M2** solo vía socio tokenizador y después de K9.

M3 se descarta.

## Condiciones del piloto (todas deben cumplirse; detalle en `08`)

- **Día 60 (2026-12-18):**
  - K1: ≥ 5 LOI no vinculantes de emisores sobre ≥ 20 contactados.
  - K2: ≥ 2 socios autorizados con term sheet no vinculante.
- **Día 90 (2027-01-17):**
  - K3: costo total de una emisión de USD 300k ≤ 6%, con 3 cotizaciones.
  - K4: dictamen escrito que confirme M1 sin registro propio, o con registro de costo ≤ USD 150k y plazo ≤ 9 meses.
  - K7: ≥ 3 de 5 emisores aceptan fee ≥ 1,5% o ≥ USD 3.000.
  - K8: ≥ 30% de los proyectos pasan la DD mínima.
- **Día 180 (2027-04-17):**
  - K9: primera colocación ejecutada **por el socio**, ≥ 70% del monto objetivo.
  - K12: margen de contribución por emisión > 0.
- **Gasto hasta el día 90:** solo entrevistas, dictamen legal y landing (pauta tope de USD 3.000, a confirmar por el responsable). Prohibido desarrollar smart contracts, custodia o secundario.

## Evidencia que cambiaría cada conclusión

| Conclusión | La revierte… |
|---|---|
| NO-GO del marketplace tokenizado minorista | CAC por inversor activo ≤ USD 50 medido en un canal propio, recurrencia ≥ 3 por año y ticket ≥ USD 1.500 (`05`, Sensibilidad, tabla 3) **y** un dictamen favorable para M2 con costo de licencias medido |
| El problema es de originación, no de distribución | Entrevistas con ALyC/PFC (`07`) que muestren que les sobran emisores calificados y les faltan inversores |
| Blockchain sin valor incremental | Un socio PSAV que muestre CAC o conversión significativamente mejores en su canal para RWA, con datos de Landtoken I u otra emisión |
| PILOTO de M1 | Dictamen de que el fee de originación por éxito exige registro costoso (K4), o < 2 socios interesados (K2) → pasar a M0 o a NO-GO total |
| M3 descartado | Que la CNV convierta el sandbox en régimen permanente con interoperabilidad amplia **y** que haya volumen secundario verificable en tokens RWA locales |

## Supuestos críticos

1. Existen pymes no inmobiliarias con flujos documentables que hoy no llegan al mercado de capitales por costo o complejidad, y no por falta de calidad crediticia.
2. Los operadores autorizados pagan por la originación y es legal que lo hagan.
3. El costo de estructurar emisiones de USD 0,3–1 M puede quedar por debajo del 6–10% del monto.
4. La norma no cambia en contra durante el piloto (hubo más de 10 RG relevantes en unos 30 meses, A8).
