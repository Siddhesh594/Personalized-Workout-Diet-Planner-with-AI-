# utils.py
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key="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")

def generate_fitness_plan(user_input: str) -> str:
    """
    Generates a personalized AI fitness plan using ChatGPT.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # fast and cheap model
            messages=[
                {"role": "system", "content": "You are a professional fitness trainer."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error generating fitness plan: {e}"
