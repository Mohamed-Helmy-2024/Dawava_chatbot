"""
FastAPI application entry point.
Run with:
    uvicorn app.main:app 
"""

from fastapi import FastAPI

from app.controllers.chat_controller import router as chat_router

app = FastAPI(title="Medical Chatbot API")

app.include_router(chat_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
