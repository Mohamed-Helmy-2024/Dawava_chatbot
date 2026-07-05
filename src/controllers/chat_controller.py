"""
Chat controller - exposes the chatbot as a FastAPI endpoint.
The client sends user_id, session_id, the required query string, and the
full conversation history as messages (up to 1000 entries).
"""

from fastapi import APIRouter
from src.schemas.chat_request import ChatRequest
from src.schemas.chat_response import ChatResponse
from src.services.chat_service import handle_chat

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Build history from the provided messages list.
    history = [
        {"role": m.role, "content": m.content}
        for m in request.messages
    ]

    result = handle_chat(
        query=request.query,
        history=history,
        user_id=request.user_id,
        session_id=request.session_id,
    )
    return result
