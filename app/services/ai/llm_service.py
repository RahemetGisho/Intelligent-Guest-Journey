import google.generativeai as genai
from app.core.config import settings
from app.services.ai.prompt_builder import build_prompt

# ✅ Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

# ✅ Define model (THIS WAS MISSING)
model = genai.GenerativeModel("gemini-1.5-flash")


async def generate_response(user_input: str, user_profile: dict) -> str:
    try:
        prompt = build_prompt(user_input, user_profile)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"