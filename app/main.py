from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import chat, room, guest, admin, auth, sentiment

app = FastAPI(title=settings.APP_NAME)

# THE MASTER KEY: This MUST be the first thing after 'app = FastAPI()'
# In app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Keep this as asterisk
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"], # Add this line
)

@app.get("/")
def root():
    return {"message": "Backend is running and CORS is wide open"}

# Include routers AFTER the middleware
app.include_router(chat.router, prefix="/chat", tags=["AI Chat"])
app.include_router(room.router, prefix="/room", tags=["Room Control"])
app.include_router(guest.router, prefix="/guest", tags=["Guest Journey"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(sentiment.router, prefix="/sentiment", tags=["Sentiment"])