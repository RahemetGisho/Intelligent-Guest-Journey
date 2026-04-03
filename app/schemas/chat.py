from pydantic import BaseModel
from datetime import datetime

class ChatCreate(BaseModel):
    user_id: str
    message: str
    response: str
    sentiment: str

class ChatRead(ChatCreate):
    timestamp: datetime

    class Config:
        orm_mode = True