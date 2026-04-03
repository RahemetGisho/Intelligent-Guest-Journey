def send_alert(user_id: str, message: str):
    """
    Simulate alert to staff
    (later: WhatsApp, email, dashboard)
    """

    print("🚨 ALERT TRIGGERED 🚨")
    print(f"Guest ID: {user_id}")
    print(f"Issue: {message}")