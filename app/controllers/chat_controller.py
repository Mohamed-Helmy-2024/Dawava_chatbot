"""
Chat controller - exposes the chatbot as a FastAPI endpoint.
The client sends the query plus the conversation history with every
request (no database, no user_id/session_id).
"""

from fastapi import APIRouter
from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse
from app.services.chat_service import handle_chat

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = handle_chat(
        query=request.query,
        history=request.history
    )
    return result
