from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.chat import Chat

router = APIRouter()

@router.get("/alerts")
def get_negative_chats(db: Session = Depends(get_db)):
    """
    Return all chats flagged as negative sentiment for staff review
    """
    alerts = db.query(Chat).filter(Chat.sentiment == "negative").all()
    return [{"user_id": c.user_id, "message": c.message, "timestamp": c.timestamp} for c in alerts]