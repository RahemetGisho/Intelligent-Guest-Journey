# create_tables.py
from app.db.session import engine, Base
from app.models import user, room, chat

Base.metadata.create_all(bind=engine)