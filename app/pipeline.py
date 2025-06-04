import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key from the environment file
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_pipeline(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]
