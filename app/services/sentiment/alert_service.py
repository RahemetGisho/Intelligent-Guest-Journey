def send_alert(user_id: str, message: str):
    """
    Simulate alert to staff
    (later: WhatsApp, email, dashboard)
    """

    print("\n" + "="*30)
    print("🚨 ALERT TRIGGERED 🚨")
    print(f"Guest ID: {user_id}")
    print(f"Issue Summary: {message}")
    print("="*30 + "\n")
    
    # Returning a dict so you can track the status in the logs if needed
    return {"status": "alert_sent", "target": "staff_dashboard"}
