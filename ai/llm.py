from google import genai
from config_folder.settings import (
    GEMINI_API_KEY,
    AI_MODEL_VERSION
    )
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt):


    try:

        response = client.models.generate_content(
            model=AI_MODEL_VERSION,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"LLM Error: {e}"

