from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.chat import Chat
from app.services.sentiment.sentiment_analyzer import analyze_sentiment

router = APIRouter()

@router.post("/analyze")
def analyze_message(user_id: str, message: str, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(message)
    chat = Chat(user_id=user_id, message=message, response="", sentiment=sentiment)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return {"sentiment": sentiment, "chat_id": chat.id}

@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(Chat).filter(Chat.sentiment == "negative").all()
    return [{"user_id": c.user_id, "message": c.message, "timestamp": c.timestamp} for c in alerts]