"""Mock del agente FinIA: lee la petición y escribe una respuesta de prueba.

No usa internet ni API key. Sirve para probar la primera rebanada vertical:
entrada -> validación -> salida.
"""

import json
from pathlib import Path

request_path = Path("data/agent_request.json")
response_path = Path("data/agent_response.json")

request = json.loads(request_path.read_text(encoding="utf-8"))

if "question" not in request or "user_id" not in request:
    raise SystemExit("Petición inválida: faltan campos obligatorios (400)")

response = {
    "answer": f"Recibí tu pregunta: {request['question']}",
    "sources": ["mock_source"],
    "needs_approval": True,
}

response_path.write_text(
    json.dumps(response, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print("Respuesta mock generada")