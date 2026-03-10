# utils.py
import google.genai as genai

# Initializing Gemini client with  API key
client = genai.Client(api_key = "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")
def generate_fitness_plan(user_input: str) -> str:
    """
    Generates a personalized AI fitness plan using Google Gemini API.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # or gemini-2.5-flash if available
            contents=user_input
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error generating fitness plan: {e}"





