# Contrato de la API — FinIA v0.1

## GET /health

- Entrada: ninguna
- Salida: `{"status": "ok"}`
- Estados: 200

## POST /agent/ask

- Entrada: `question`, `user_id`, `context`
- Salida: `answer`, `sources`, `needs_approval`
- Estados: 200, 400, 500

### Campos

| Campo | Tipo | Obligatorio | Para qué sirve |
| --- | --- | --- | --- |
| question | texto | sí | Pregunta del usuario sobre sus finanzas |
| user_id | texto | sí | Identificar el contexto permitido |
| context | objeto | no | Cuenta y periodo consultado |
| answer | texto | sí (salida) | Respuesta del agente |
| sources | arreglo | sí (salida) | Trazabilidad: de dónde salieron los montos |
| needs_approval | booleano | sí (salida) | Marca que la acción requiere aprobación humana |

### Reglas del contrato

- Si `needs_approval` es `true`, la API entrega un borrador: nunca ejecuta el
  movimiento de dinero.
- Si faltan datos suficientes, la respuesta indica el faltante en vez de
  inventar cifras.
- Todos los montos citados en `answer` deben existir en `sources`.

No implementado todavía: primero se acuerda la interfaz, después se escribe el
código y se conecta el modelo (clase 5).
