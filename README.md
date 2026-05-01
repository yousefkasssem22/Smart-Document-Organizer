# 🧠 Smart Document Organizer

AI-powered document analysis system that processes files (TXT, PDF, DOCX) and extracts structured insights using a local LLM via **Ollama (TinyLlama)**.

---

## 🚀 Features

* 📄 Upload and analyze documents (TXT, PDF, DOCX)
* 🧠 AI-based content understanding
* 🏷️ Automatic tagging and classification
* 🌐 REST API using FastAPI
* ⚡ Local LLM inference using Ollama 

---

## 🏗️ Architecture

```
Client (Swagger / Frontend)
        ↓
FastAPI Backend
        ↓
Document Router (/api/analyze)
        ↓
Processing Pipeline (pipeline.py)
        ↓
Ollama API (TinyLlama model)
        ↓
Structured JSON Response
```

---

## 📂 Project Structure

```
smart-document-organizer/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── routes/
│   │   └── document.py     # API endpoints
│   ├── services/
│   │   └── pipeline.py     # AI processing logic
│   ├── models/             # Data models (optional)
│   └── utils/              # Helpers
│
├── venv/                   # Virtual environment
├── .env                    # Environment variables
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Ollama (TinyLlama)
* **HTTP Client:** requests
* **File Handling:** python-multipart
* **Environment:** python-dotenv

---

## 🧠 How It Works

1. User uploads a file via `/api/analyze`
2. Backend reads and extracts text
3. Text is sent to Ollama (TinyLlama)
4. Model returns structured JSON:

   ```json
   {
     "type": "document type",
     "summary": "short summary",
     "tags": ["tag1", "tag2"],
     "language": "en"
   }
   ```
5. API returns final response

---

## 🧪 API Endpoint

### 🔹 Analyze Document

**POST** `/api/analyze`

#### Request:

* `multipart/form-data`
* file: document file

#### Response:

```json
{
  "file_name": "example.txt",
  "status": "success",
  "analysis": {
    "type": "text",
    "summary": "This document talks about...",
    "tags": ["ai", "document"],
    "language": "en"
  }
}
```

---

## 🖥️ Installation

### 1. Clone repo

```bash
git clone <repo-url>
cd smart-document-organizer
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download from:
👉 https://ollama.com

---

### 5. Pull TinyLlama model

```bash
ollama pull tinyllama
```

---

## ▶️ Run the Project

### Terminal 1 (Ollama):

```bash
ollama serve
```

### Terminal 2 (Backend):

```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

---

## 🌐 Open API Docs

👉 http://127.0.0.1:8000/docs

---

## ⚠️ Notes

* TinyLlama is lightweight → responses may not always be perfectly structured
* JSON parsing fallback is implemented for robustness
* Large files are truncated before sending to model

---

## 🔮 Future Improvements

* Use stronger LLM (Mistral / LLaMA 3)
* Add vector database (RAG)
* Store processed documents in DB
* Add frontend dashboard
* Support OCR for images

---

## 👨‍💻 Author

**Yousef Kassem**

---

## ⭐ License

MIT License
