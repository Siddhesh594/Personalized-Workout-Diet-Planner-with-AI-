# utils.py
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

def generate_fitness_plan(user_input: str):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional fitness trainer."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
