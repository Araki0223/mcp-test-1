from pydantic import BaseModel
from typing import List, Dict, Optional

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class MCPRequest(BaseModel):
    thread_id: str
    messages: List[Message]
    context: Optional[Dict] = {}

class MCPResponse(BaseModel):
    content: str
