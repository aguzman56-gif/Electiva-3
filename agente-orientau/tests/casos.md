# Casos de validación — v0.1

| # | Caso | Resultado esperado |
| --- | --- | --- |
| 1 | `python -m json.tool data/agent_request.json` | JSON válido, sin error |
| 2 | `python -m json.tool data/agent_response.json` | JSON válido, sin error |
| 3 | Petición sin el campo `question` | 400, petición inválida |
| 4 | Usuario sin historial de transacciones | El agente indica el faltante, no inventa cifras |
| 5 | Respuesta que propone mover dinero | `needs_approval` en `true` |
| 6 | Revisión del repositorio | No existe ninguna clave real versionada |
