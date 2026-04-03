from sqlalchemy import Column, String, Integer, Boolean
from app.db.session import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(String, primary_key=True, index=True)
    temperature = Column(Integer, default=24)
    lights_on = Column(Boolean, default=True)