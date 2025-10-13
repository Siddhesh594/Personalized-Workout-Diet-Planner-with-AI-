# utils.py
import google.genai as genai

# Initialize Gemini client with your API key
client = genai.Client(api_key="AIzaSyBy-EJ2hLyKDkLjDJ2ZAbaozRqWFAxpU2Q")

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
