from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    id: str
    name: str
    travel_type: Optional[str] = "solo"
    food_pref: Optional[str] = "any"

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    class Config:
        orm_mode = True