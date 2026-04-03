def build_prompt(user_input: str, user_profile: dict) -> str:
    """
    Builds a smart prompt for the AI Concierge
    """

    # Extract user info
    name = user_profile.get("name", "Guest")
    preferences = user_profile.get("preferences", {})
    travel_type = preferences.get("travel_type", "solo")
    food = preferences.get("food", "any")
    mood = preferences.get("mood", "neutral")

    # Resort knowledge (hardcoded for hackathon)
    resort_info = """
    You are an AI concierge for a luxury Ethiopian resort.
    
    Resort features:
    - Spa (9 AM – 9 PM)
    - Traditional Ethiopian restaurant
    - Coffee ceremony experience
    - City tours (Entoto, cultural markets)
    - Swimming pool and kids play area
    
    You must:
    - Be polite and professional
    - Give personalized recommendations
    - Keep answers short and helpful
    """

    # Final prompt
    prompt = f"""
    {resort_info}

    Guest Info:
    - Name: {name}
    - Travel Type: {travel_type}
    - Food Preference: {food}
    - Mood: {mood}

    Guest says:
    "{user_input}"

    Respond as a helpful luxury concierge.
    """

    return prompt