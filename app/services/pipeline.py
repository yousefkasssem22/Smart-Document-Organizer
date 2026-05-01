import json
import requests

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
        
        if response.status_code != 200:
            return {
                "file_name": file.filename,
                "error": f"Ollama Error {response.status_code}"
            }

        result = response.json()
        parsed = json.loads(result.get("response", "{}"))

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