# FinIA — Agente de finanzas personales

Prototipo académico de un agente que analiza las transacciones del usuario,
explica en qué está gastando de más y prepara borradores de movimientos de
dinero (ahorro o transferencia) que el usuario debe aprobar.

Electiva III · Cloud Computing — Universidad Antonio Nariño
Estado: base técnica v0.1 — la respuesta es simulada (mock), todavía no hay
modelo de IA conectado.

## Límite del agente

FinIA nunca ejecuta un movimiento de dinero. Opera con permisos de solo
lectura sobre las cuentas y solo genera borradores que requieren aprobación
explícita del usuario.

## Estructura

- `app/` — código o mock del agente
- `data/` — contratos JSON de entrada y salida
- `docs/` — contrato de la API
- `tests/` — casos de validación
- `.env.example` — nombres de variables, sin claves reales
- `.gitignore` — archivos que no se versionan

## Cómo ejecutar

1. Copiar `.env.example` a `.env` y completar los valores localmente.
2. Validar los contratos JSON:
   `python -m json.tool data/agent_request.json`
   `python -m json.tool data/agent_response.json`
3. Ejecutar el mock: `python app/mock_agent.py`

No se necesita API key para esta versión.

## Integrantes

- (nombre)
- (nombre)
- (nombre)
