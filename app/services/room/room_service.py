from app.services.room.mqtt_client import publish, connect

# Connect client when service starts
connect()

async def set_temperature(room_id: str, value: int):
    """
    Simulate adjusting room temperature via MQTT
    """
    topic = f"resort/room/{room_id}/temperature"
    # We wrap this in async to keep the main route happy
    publish(topic, str(value))
    print(f"--- [MQTT PUBLISH] --- Topic: {topic} | Value: {value}°C")
    return f"Room {room_id} temperature set to {value}°C"


async def toggle_light(room_id: str, state: str):
    """
    Turn lights on/off via MQTT
    """
    topic = f"resort/room/{room_id}/light"
    publish(topic, state)
    print(f"--- [MQTT PUBLISH] --- Topic: {topic} | State: {state.upper()}")
    return f"Room {room_id} light turned {state}"