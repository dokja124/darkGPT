from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

LIARA_BASE_URL = "https://ai.liara.ir/api/6940fe21363673561d9a83cb/v1"
LIARA_API_KEY = os.getenv("LIARA_API_KEY")
LIARA_MODEL = "google/gemini-2.0-flash-001"

client = OpenAI(base_url=LIARA_BASE_URL, api_key=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)

def generate_with_liara(full_prompt):
    try:    
        completion = client.chat.completions.create(
            model=LIARA_MODEL,
            messages=[
            # {
            #     "role": "system",
            #     "content": os.environ.get("SYSTEM_PROMPT")
            # },
            {
                "role": "user",
                "content": full_prompt
            },
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None
