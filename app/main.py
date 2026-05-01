from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.routes.document import router as document_router
import requests
import json

# Ollama local endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

app = FastAPI(
    title="Smart Document Organizer",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# existing routes
app.include_router(document_router, prefix="/api", tags=["documents"])


@app.post("/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    prompt = f"""
{text[:50]}"""


    payload = {
        "model": "tinyllama",  # 👈 ممكن تغيرها لـ mistral
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)

        if response.status_code != 200:
            return {
                "error": "Ollama request failed",
                "status_code": response.status_code,
                "details": response.text[:300]
            }

        result = response.json()
        ai_text = result.get("response", "{}")

        try:
            parsed = json.loads(ai_text)
        except:
            parsed = {
                "type": "unknown",
                "summary": ai_text[:300],
                "tags": ["fallback"]
            }

    except Exception as e:
        return {
            "error": "Server error",
            "details": str(e)
        }

    return {
        "filename": file.filename,
        "analysis": parsed
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}