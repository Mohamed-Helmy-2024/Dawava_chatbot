from typing import List, Dict, Any
from pydantic import BaseModel

class ChatResponse(BaseModel):
    # classification: str
    # retrieved_context: List[Dict[str, Any]]
    answer: str
