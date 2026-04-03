from fastapi import APIRouter, Depends
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.services.ai.llm_service import generate_response
from app.services.sentiment.sentiment_analyzer import analyze_sentiment
from app.services.sentiment.alert_service import send_alert
from app.services.room.room_service import set_temperature, toggle_light
from app.services.recommendation.recommender import recommend_activities, recommend_food
from app.db.session import get_db
from app.models.user import User
from app.models.chat import Chat

router = APIRouter()


# ✅ Request schema for guest interaction
class GuestMessage(BaseModel):
    user_id: str
    name: str
    room_id: str
    message: str
    preferences: Optional[dict] = {}  # e.g., {"travel_type": "family", "food": "spicy"}


# ✅ Endpoint logic with DB + Recommendation integration
@router.post("/interact")
async def guest_interact(payload: GuestMessage, db: Session = Depends(get_db)):

    # 1️⃣ Check if user exists
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        user = User(
            id=payload.user_id,
            name=payload.name,
            travel_type=payload.preferences.get("travel_type", "solo"),
            food_pref=payload.preferences.get("food", "any")
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # 2️⃣ Sentiment analysis
    sentiment = analyze_sentiment(payload.message)
    if sentiment == "negative":
        send_alert(user.id, payload.message)

    # 3️⃣ AI Concierge response
    user_profile = {"name": user.name, "preferences": payload.preferences}
    ai_response = await generate_response(payload.message, user_profile)

    # 4️⃣ Smart room automation triggers
    room_actions = []
    if "hot" in payload.message.lower():
        room_actions.append(set_temperature(payload.room_id, 22))
    if "dark" in payload.message.lower():
        room_actions.append(toggle_light(payload.room_id, "on"))

    # 5️⃣ Save chat to DB
    chat = Chat(
        user_id=user.id,
        message=payload.message,
        response=ai_response,
        sentiment=sentiment
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)

    # 6️⃣ Recommendation System
    past_chats = db.query(Chat).filter(Chat.user_id == user.id).all()
    past_activities = [c.message for c in past_chats if "activity" in c.message.lower()]
    past_foods = [c.message for c in past_chats if "food" in c.message.lower()]

    activities = recommend_activities(user.travel_type, past_activities)
    foods = recommend_food(user.food_pref, past_foods)

    return {
        "ai_response": ai_response,
        "sentiment": sentiment,
        "room_actions": room_actions,
        "recommendations": {
            "activities": activities,
            "foods": foods
        }
    }