from app.services.room.mqtt_client import publish, connect

# Connect client when service starts
connect()


def set_temperature(room_id: str, value: int):
    """
    Simulate adjusting room temperature
    """
    topic = f"resort/room/{room_id}/temperature"
    publish(topic, str(value))
    return f"Room {room_id} temperature set to {value}°C"


def toggle_light(room_id: str, state: str):
    """
    Turn lights on/off
    """
    topic = f"resort/room/{room_id}/light"
    publish(topic, state)
    return f"Room {room_id} light turned {state}"