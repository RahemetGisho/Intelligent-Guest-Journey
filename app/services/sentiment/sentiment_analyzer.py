def analyze_sentiment(text: str) -> str:
    """
    Very simple rule-based sentiment (hackathon-ready)
    Later you can upgrade to Gemini
    """

    negative_words = [
        "tired", "bad", "angry", "upset",
        "hot", "cold", "not working",
        "hate", "frustrated", "annoyed"
    ]

    text_lower = text.lower()

    for word in negative_words:
        if word in text_lower:
            return "negative"

    # Fixed: Removed the trailing comma to ensure it returns a string, not a tuple
    return "positive"