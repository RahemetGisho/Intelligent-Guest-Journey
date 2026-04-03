from fastapi import APIRouter
from app.services.ai.llm_service import generate_response
from app.services.sentiment.sentiment_analyzer import analyze_sentiment
from app.services.sentiment.alert_service import send_alert

router = APIRouter()


@router.post("/chat")
async def chat():

    # Simulated user
    user = {
        "id": "123",
        "name": "Kulle",
        "preferences": {
            "travel_type": "family",
            "food": "spicy",
            "mood": "tired"
        }
    }

    user_input = "The room is too hot and I'm really tired"

    # 🧠 Step 1: Sentiment analysis
    sentiment = analyze_sentiment(user_input)

    # 🚨 Step 2: Trigger alert if negative
    if sentiment == "negative":
        send_alert(user["id"], user_input)

    # 🤖 Step 3: AI response
    response = await generate_response(user_input, user)

    return {
        "response": response,
        "sentiment": sentiment
    }