from typing import List
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """A single turn in the conversation history."""
    role: str  # "human" or "ai"
    content: str


class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    query: str = Field(..., min_length=1)
    messages: List[ChatMessage] = Field(default_factory=list)
