from sqlalchemy import Column, String, Integer
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    travel_type = Column(String, default="solo")
    food_pref = Column(String, default="any")