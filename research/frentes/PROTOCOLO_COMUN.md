# Protocolo común para frentes (A1–A9)

- Fecha de ejecución: 2026-10-19 (Argentina). Idioma: español rioplatense técnico.
- Leer MANDATO_CLAUDE.md y SCHEMA_EVIDENCIA.json en la raíz del repo.
- Todo número o hecho externo: URL pública consultada + fecha + ámbito. Nada de bibliografía inventada.
- Separar: hecho verificado / declaración comercial / inferencia / opinión.
- Evidencia: cada frente escribe `research/frentes/<FRENTE>_evidencia.csv`, separador `;`, encabezado:
  `id;claim;url;publisher;published_at;accessed_at;type;confidence;notes;confirmation_status`
  - IDs por rango: A1=E1001.., A2=E2001.., A3=E3001.., A5/A7=E5001.., A8=E8001.., A9=E9001..
  - type ∈ regulacion_oficial|registro_oficial|documento_primario_empresa|fuente_secundaria|inferencia|declaracion_comercial
  - confidence ∈ alta|media|baja ; confirmation_status ∈ verificado|pendiente|contradictorio|no_verificable
  - accessed_at en ISO 8601 date-time (ej. 2026-10-19T12:00:00-03:00); published_at YYYY-MM-DD o vacío.
  - No usar `;` dentro de campos (reemplazar por `,`).
- Si una URL no carga (403, timeout), registrarlo como enlace roto en el informe del frente; no inventar contenido.
- PROHIBIDO: crear cuentas, enviar formularios, contactar terceros, invertir, publicar. Solo lectura.
