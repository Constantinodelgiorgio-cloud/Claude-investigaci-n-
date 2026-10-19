# 04 — Mapa de procesos (A6 Producto/procesos)

**Fecha:** 2026-10-19 · **Estado:** diseño conceptual, no validado jurídicamente.
**Regla de lectura:** cada paso marcado `[REG]` es una función regulada que, según el dictamen preliminar (`03_DICTAMEN_REGULATORIO_PRELIMINAR.md`), debe ejecutarla un sujeto inscripto ante CNV (PFC, ALyC/AN, ACVN, fiduciario financiero o PSAV según el caso). El marketplace (en adelante **MKT**) solo ejecuta pasos no marcados. La asignación exacta es **hipótesis para abogado** (ver `11_PREGUNTAS_PARA_ABOGADO_Y_OPERADORES.md`).

## 1. Dos productos distintos que no deben mezclarse

| | MVP informativo/comercial (M0/M1) | Producto financiero regulado (M2/M3) |
|---|---|---|
| Qué hace MKT | Origina, filtra, documenta y deriva emisores/inversores a un operador autorizado | Opera colocación, registro, custodia y/o negociación |
| Recibe dinero | **No** | Sí (vía entidad autorizada) |
| Recibe órdenes | **No** | Sí |
| Recomienda inversiones | **No** (solo información estandarizada y verificada) | Según figura (asesoramiento requiere habilitación) |
| Token | No necesario | Opcional, solo si aporta valor medible (ver `06`) |
| Ingreso | Fee B2B al operador/emisor por originación y preparación documental | Comisión de colocación, administración, negociación |

## 2. Actores

- **Emisor:** pyme/desarrollador titular del proyecto productivo.
- **MKT:** marketplace / originador.
- **OP:** operador autorizado (PFC registrada en CNV para crowdfunding; ALyC/AN para colocación de valores negociables; fiduciario financiero inscripto si hay fideicomiso; PSAV si hay activos virtuales; ACVN para registro/custodia de valores).
- **EST:** estructurador legal/financiero (estudio jurídico, fiduciario).
- **AUD:** auditor/contador certificante; eventualmente calificadora.
- **INV:** inversor (minorista o calificado).
- **CNV:** autoridad de aplicación. **UIF:** autoridad AML.

## 3. Journey del emisor (end-to-end)

| # | Paso | Responsable | Documentos/insumos | Salida | Control/gate |
|---|---|---|---|---|---|
| E1 | Alta y pre-calificación (formulario) | MKT | Constancia CUIT, estatuto, balances 2 ejercicios, descripción del proyecto, uso de fondos | Ficha preliminar | Filtros duros: CUIT activo, sin sanciones, sin juicios relevantes (consulta pública), rubro admitido |
| E2 | KYB / identificación de beneficiarios finales | MKT (pre-screen) + OP `[REG]` (KYC formal UIF) | DNI de autoridades, BF ≥ umbral UIF, listas PEP/terroristas | Legajo KYB | OP decide; MKT no reemplaza la debida diligencia del sujeto obligado |
| E3 | Due diligence del proyecto | MKT + EST | Plan de negocios, flujo de fondos proyectado, títulos/contratos, permisos, seguros | Informe de DD con matriz de riesgos | Comité de admisión MKT (criterios publicados, conflicto de interés declarado) |
| E4 | Elección de instrumento y estructura | EST + OP `[REG]` | Comparativa: ON pyme, fideicomiso financiero, acciones vía PFC, cheque/pagaré avalado (SGR), préstamo vía PFC | Term sheet | Que el instrumento otorgue derechos jurídicos exigibles **fuera** del token |
| E5 | Documentación de oferta (prospecto/ficha de proyecto, factores de riesgo) | EST + OP `[REG]` | Modelos CNV según figura | Documento de oferta | Revisión legal; leyenda de riesgos |
| E6 | Autorización / inscripción de la oferta | OP `[REG]` ante CNV | Según régimen (automático o con revisión) | Oferta autorizada | **Gate duro**: sin autorización no hay campaña |
| E7 | (Opcional) Representación tokenizada | OP/PSAV/ACVN `[REG]` + proveedor tecnológico | Smart contract auditado, whitelist, política de llaves | Token espejo del registro legal | Solo si `06` demuestra valor; reconciliación diaria registro legal ↔ on-chain |
| E8 | Campaña | OP `[REG]` (oferta); MKT (difusión de información **dentro de lo que el abogado admita**) | Material publicitario revisado | Página de oferta | Publicidad revisada por OP; MKT no promete rendimientos |
| E9 | Cierre: alcanzado/no alcanzado | OP `[REG]` | Acta de cierre | Fondos al emisor o devolución | Fondos nunca pasan por MKT |
| E10 | Uso de fondos y reporting periódico | Emisor → OP; MKT publica resumen estandarizado | Estados contables, hitos, desvíos | Reportes trimestrales | Alertas por incumplimiento de plazos |
| E11 | Pagos (intereses, dividendos, flujos fiduciarios) | Emisor → agente de pago/fiduciario `[REG]` | Cronograma | Pagos a INV | Conciliación pública de pagos vs. cronograma |
| E12 | Eventos de crédito / default | Fiduciario/OP `[REG]`; asamblea de tenedores | Contrato, garantías | Ejecución/reestructuración | Protocolo de comunicación publicado de antemano |
| E13 | Salida (amortización final, recompra, venta) | OP `[REG]` / mercado | — | Cancelación | Registro de baja |

## 4. Journey del inversor

| # | Paso | Responsable | Notas |
|---|---|---|---|
| I1 | Descubrimiento (catálogo, filtros, fichas estandarizadas) | MKT | Información verificada y fechada; sin ranking de "mejores inversiones" |
| I2 | Educación y test de conveniencia/idoneidad | OP `[REG]` (perfil del inversor) | MKT puede ofrecer contenido educativo genérico |
| I3 | Onboarding y KYC | OP `[REG]` | Redirección a OP; MKT no almacena documentación KYC salvo contrato de encargado de tratamiento (Ley 25.326) |
| I4 | Suscripción / orden | OP `[REG]` | MKT no recibe órdenes |
| I5 | Integración de fondos | OP `[REG]` (cuenta comitente/cuenta de la PFC) | — |
| I6 | Registro de titularidad | ACVN/agente de registro/fiduciario `[REG]` (+ token espejo opcional) | El token no crea derechos por sí mismo: el derecho surge del instrumento y del registro legal |
| I7 | Reportes, cobros, impuestos | OP + emisor; MKT agrega vistas | — |
| I8 | Reclamos | OP (canal de atención obligatorio) + MKT (canal propio de calidad de información) | Escalamiento a CNV / defensa del consumidor |
| I9 | Salida/secundario | Mercado autorizado `[REG]` o ninguno | Advertir iliquidez desde I1 |

## 5. BPMN conceptual (texto)

```
[Emisor] --(alta)--> {MKT: pre-calificación} --rechazo--> (fin)
      \--aprobado--> {MKT+EST: DD} --> <Comité MKT> --no--> (fin)
                                          |sí
                                          v
                 {EST+OP: estructura + doc. oferta} --> <<OP: autorización CNV>> --denegada--> (fin)
                                                              |ok
                                                              v
   [Inversor] --> {MKT: catálogo} --> link --> <<OP: KYC + idoneidad>> --> <<OP: suscripción + fondos>>
                                                              |
                                          <<OP: cierre>> --no alcanzado--> <<OP: devolución>>
                                                              |alcanzado
                                                              v
                       <<Fiduciario/OP: fondos al emisor>> --> {Emisor: ejecución} --> {reporting}
                                                              |
                                  <<Agente de pago: flujos>> --> <<salida/amortización>> --> (fin)
Leyenda: {…} tarea no regulada · <<…>> tarea regulada [REG] · <…> decisión
```

## 6. RACI (R = ejecuta, A = responsable final, C = consultado, I = informado)

| Actividad | MKT | OP | EST | Emisor | INV | AUD |
|---|---|---|---|---|---|---|
| Pre-calificación emisor | R/A | I | C | C | – | – |
| KYC/KYB formal (UIF) | C | R/A | – | C | C | – |
| Due diligence de proyecto | R | A | C | C | – | C |
| Estructuración del instrumento | C | A | R | C | – | C |
| Documento de oferta | C | A | R | R | – | C |
| Autorización CNV | I | R/A | C | C | – | – |
| Publicidad de la oferta | C | A | – | C | I | – |
| Recepción de órdenes y fondos | – | R/A | – | I | R | – |
| Registro de titularidad / token | I | A | – | – | I | – |
| Reporting periódico | R (agregación) | A | – | R | I | C |
| Pagos a inversores | I | A | – | R | I | – |
| Gestión de default | I | A | C | R | C | – |
| Reclamos de inversores | C | R/A | – | C | – | – |

## 7. Disputas y conflictos

- MKT publica política de conflictos (no invierte en proyectos listados; si cobra al emisor, lo informa en cada ficha).
- Toda controversia sobre el instrumento se rige por su documento (jurisdicción, tribunal arbitral si está previsto); MKT no es parte del contrato de inversión.
- Registro de auditoría (audit trail) inmutable de toda información publicada y sus versiones (ver `06`).
