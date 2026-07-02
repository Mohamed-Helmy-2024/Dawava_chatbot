from typing import List, Dict
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    query: str
    history: List[Dict[str, str]] = Field(default_factory=list)
