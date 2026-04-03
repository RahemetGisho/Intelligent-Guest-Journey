from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import chat
from app.api.routes import room
from app.api.routes import guest
from app.api.routes import admin, auth, sentiment


app = FastAPI(title=settings.APP_NAME)

app.include_router(chat.router, prefix="/chat", tags=["AI Chat"])
app.include_router(room.router, prefix="/room", tags=["Room Control"])
app.include_router(guest.router, prefix="/guest", tags=["Guest Journey"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(sentiment.router, prefix="/sentiment", tags=["Sentiment"])


@app.get("/")
def root():
    return {"message": "Backend running "}


