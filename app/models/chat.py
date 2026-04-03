from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    message = Column(String)
    response = Column(String)
    sentiment = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())