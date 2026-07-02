Here is your **clean formatted README (Docker-only usage)**:

---

# Dawava Chatbot API

A FastAPI-based chatbot backend powered by LLMs, memory management, and FAISS vector search, fully containerized using Docker.

---

## Features

* FastAPI backend
* Conversation memory support
* LLM-powered responses (Cohere / compatible models)
* FAISS vector database for embeddings
* Dockerized deployment
* REST API (`/chat` endpoint)

---

## Project Structure

```text id="kq8x3b"
CHATBOT_API/
│
├── app/
│   ├── core/
│   ├── controllers/
│   ├── services/
│   ├── models/
│   └── main.py
|   └── config.py
│
├── data/
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## Run with Docker (Only Method)

### 1. Build Docker Image

Run this inside the project directory (where Dockerfile exists):

```
docker build -t dawava-chatbot-api .
```

---

### 2. Remove Existing Container (if any)

```
docker rm -f chatbot
```

---

### 3. Run Container

```
docker run -d -p 8000:8000 --name chatbot dawava-chatbot-api
```

---

### 4. Check Running Container

```
docker ps
```

---

### 5. Stop Container

```
docker stop chatbot
```

---

### 6. Remove Container

```
docker rm -f chatbot
```

---

### 7. List Images

```
docker images
```

---

## API Usage

### Endpoint

```
[POST /chat](http://localhost:8000/docs#/default/chat_chat_post)
```

---

### Example Request

```json
{
  "query": "what drug I take every morning?",
  "history": [
    {
      "role": "human",
      "content": "Hello, my name is Ahmed."
    },
    {
      "role": "ai",
      "content": "Hello Ahmed! How can I help you today?"
    },
    {
      "role": "human",
      "content": "I have type 2 diabetes."
    },
    {
      "role": "ai",
      "content": "Thanks for letting me know. Are you taking any medication?"
    },
    {
      "role": "human",
      "content": "Yes, I take Metformin 1000 mg twice daily."
    },
    {
      "role": "ai",
      "content": "Understood. Do you have any other medical conditions?"
    },
    {
      "role": "human",
      "content": "I also have high blood pressure."
    },
    {
      "role": "ai",
      "content": "Are you taking medication for your blood pressure?"
    },
    {
      "role": "human",
      "content": "Yes, I take Amlodipine 5 mg every morning."
    }
  ]
}
```

---

### Example Response

```json
{
  "answer": "Based on our conversation, you take Amlodipine 5 mg every morning for your high blood pressure."
}
```

---

## Docker Workflow Summary

```bash id="d2x9lm"
docker build -t dawava-chatbot-api .
docker rm -f chatbot
docker run -d -p 8000:8000 --name chatbot dawava-chatbot-api
docker ps
docker stop chatbot
docker rm -f chatbot
docker images
```

---

## Notes

* Ensure `.env` file is NOT included in Docker image
* Rebuild Docker image after any code change
* FAISS data should be persisted inside `/data` if needed

---

## Tech Stack

* FastAPI
* LangChain
* Cohere / LLM APIs
* FAISS
* Docker
* Python 3.10+

---

## Author

Mohamed Helmy

---

If you want next upgrade, I can make it:

* production-ready Docker (gunicorn + uvicorn workers)
* docker-compose (API + vector DB + cache)
* CI/CD GitHub Actions auto deploy
* or professional README with badges + architecture diagram
