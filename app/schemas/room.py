from pydantic import BaseModel
from typing import Optional

class RoomBase(BaseModel):
    name: str
    room_type: str  # e.g., "single", "double", "suite"
    capacity: int
    status: Optional[str] = "available"  # available, occupied, maintenance

class RoomCreate(RoomBase):
    pass

class RoomUpdate(BaseModel):
    status: Optional[str] = None
    capacity: Optional[int] = None

class Room(RoomBase):
    id: str

    class Config:
        orm_mode = True