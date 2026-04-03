from fastapi import APIRouter
from app.services.room.room_service import set_temperature, toggle_light

router = APIRouter()


@router.post("/temperature/{room_id}/{value}")
def change_temperature(room_id: str, value: int):
    result = set_temperature(room_id, value)
    return {"message": result}


@router.post("/light/{room_id}/{state}")
def change_light(room_id: str, state: str):
    if state.lower() not in ["on", "off"]:
        return {"error": "State must be 'on' or 'off'"}
    result = toggle_light(room_id, state.lower())
    return {"message": result}