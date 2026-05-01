import json
import requests
from fastapi import APIRouter

router = APIRouter()

OLLAMA_URL = "http://localhost:11434/api/generate"

async def process_document(file):
    try:
        content = await file.read()
        text = content.decode("utf-8", errors="ignore")

        prompt = f"""Analyze this document and return ONLY a valid JSON object:
{{
    "type": "document type",
    "summary": "short summary",
    "tags": ["tag1", "tag2"],
    "language": "en"
}}

Document: {text[:4000]}"""

        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "format": "json"
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:500]}")

        if response.status_code != 200:
            return {
                "file_name": file.filename,
                "error": f"Ollama Error {response.status_code}",
                "details": response.text[:300]
            }

        result = response.json()
        ai_response = result.get("response", "{}")
        
        try:
            parsed = json.loads(ai_response)
        except json.JSONDecodeError:
            parsed = {
                "type": "unknown",
                "summary": ai_response[:500],
                "tags": ["unparsed"],
                "language": "unknown"
            }

        return {
            "file_name": file.filename,
            "status": "success",
            "analysis": parsed
        }

    except Exception as e:
        return {
            "file_name": file.filename,
            "error": str(e)
        }