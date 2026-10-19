# RWA Marketplace Argentina — paquete de investigación delegable

**Versión:** 0.1 · **Fecha de referencia:** 2026-10-19 · **Alcance:** Argentina, con benchmarks regionales e internacionales.

## Objetivo de negocio
Evaluar si existe una oportunidad real, diferenciable y jurídicamente viable para un marketplace donde titulares de proyectos productivos e instrumentos representados mediante tokens puedan conectar con inversores. La plataforma **no** se presupone emisora, intermediaria, custodio ni mercado secundario hasta clasificar regulatoriamente sus funciones.

## Cómo ejecutarlo en Claude

### Ruta más directa: Claude Cowork / Claude (tarea en la nube)
1. Abre un proyecto nuevo en Claude, titulado `Marketplace RWA Argentina — Discovery`.
2. Adjunta `MANDATO_CLAUDE.md` y `SCHEMA_EVIDENCIA.json`.
3. Pide: `Ejecutá el mandato adjunto como una tarea de investigación exhaustiva; organizá subagentes en paralelo cuando esté disponible, generá entregables y aplicá los controles de verificación. No construyas la app ni contactes a terceros.`
4. Una sesión en la nube de Cowork puede seguir trabajando cuando cerrás tu dispositivo. Para un inicio en otro horario, usá `Programadas` y una ejecución única cuando esté disponible en la interfaz, no una recurrencia innecesaria.

### Ruta más técnica: Claude Code Routines
1. Crear un repositorio **privado** y añadir `MANDATO_CLAUDE.md`, `SCHEMA_EVIDENCIA.json` y este archivo.
2. Abrir https://claude.ai/code/routines y crear una rutina `RWA ARG — Investigación inicial`.
3. Elegir repositorio, entorno con acceso a las fuentes de investigación y disparador **una sola vez** o `Run now`.
4. Deshabilitar conectores no necesarios, especialmente aquellos con escritura, y limitar permisos de git.
5. Usar como prompt de rutina: `Ejecutá de principio a fin el archivo MANDATO_CLAUDE.md; conservá resultados verificables, informes y tablas en research/; no realices transacciones ni publicaciones externas ni mensajes.`
6. Revisar las limitaciones de uso y costes y el estado final de la ejecución. La duración efectiva depende de los límites y acceso, no equivale a ocho horas garantizadas.

## Hallazgos ya verificados para orientar la búsqueda
- **RG CNV 1125/2026** (crowdfunding y oferta pública automática) https://www.argentina.gob.ar/noticias/la-cnv-habilita-el-crowdfunding-con-autorizacion-automatica-y-amplia-las-alternativas-de
- **RG CNV 1150/2026** (ampliación de tokenización) https://www.argentina.gob.ar/node/504466
- **RG CNV 1172/2026** (reordenamiento PSAV 14/10/2026) https://www.argentina.gob.ar/noticias/reordenamiento-del-marco-regulatorio-de-los-proveedores-de-servicios-de-activos-virtuales
- **RG 1165/2026** (matriz de compatibilidades) https://www.argentina.gob.ar/noticias/nueva-matriz-de-compatibilidades-para-agentes-plataformas-de-financiamiento-colectivo-psavs
- **Reglas PFC** https://www.argentina.gob.ar/normativa/recurso/219405/texact-TituloXIV-CapI/htm
- **Normas PSAV vigentes** https://www.argentina.gob.ar/normativa/recurso/219405/texact-TituloXIV-CapIII/htm
- **Metro Futuro** https://www.metro-futuro.com/proyectos
- **Crowdium** https://crowdium.ar/como-invertir
- **Trustoken** https://www.trustoken.com.ar/
- **BrickFlow** https://www.brickflow.com.ar/
- **Republic** https://republic.com/investment-opportunities

> Estos enlaces son puntos de partida y no prueban que cada servicio tenga licencias, operaciones completadas o inversiones seguras. El agente legal debe contrastar registros y estados.

## Restricciones de la investigación
Solamente investigación, lectura y producción de artefactos privados. Prohibido ofrecer inversiones, recibir fondos, emitir tokens, recomendar instrumentos personales, modificar páginas, enviar mensajes o crear cuentas sin consentimiento adicional.
