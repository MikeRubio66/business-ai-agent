import os
from fastapi import FastAPI
app = FastAPI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")
@app.get("/ask")
def ask(q: str):
    # placeholder: call to OpenAI or Gemini here
    if "ventas" in q:
        return {"answer": "Actualmente el total de ventas es $12,345 (demo)"}
    return {"answer": "Respuesta generada (demo). Configure API para respuestas reales."}
