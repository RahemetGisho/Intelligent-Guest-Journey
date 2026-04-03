import paho.mqtt.client as mqtt

# Broker info (HiveMQ public broker for testing)
BROKER = "broker.hivemq.com"
PORT = 1883

# Fix: Add callback_api_version for paho-mqtt 2.0+
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "resort_backend")

def connect():
    try:
        client.connect(BROKER, PORT)
        client.loop_start()
        return True
    except Exception as e:
        print(f"MQTT connection error: {e}")
        return False

def publish(topic: str, message: str):
    """
    Send MQTT message
    """
    try:
        client.publish(topic, message)
    except Exception as e:
        print(f"MQTT publish error: {e}")

def disconnect():
    """Clean up MQTT connection"""
    client.loop_stop()
    client.disconnect()