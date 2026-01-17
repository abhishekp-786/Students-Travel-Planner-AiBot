import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL")
API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def ask_hf(prompt):
    # Standard format for Instruct models
    payload = {
        "inputs": f"User: {prompt}\nAssistant:",
        "parameters": {"max_new_tokens": 800, "temperature": 0.7, "top_p": 0.9}
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        
        if isinstance(data, list):
            # Clean the response to only show the AI's part
            text = data[0].get("generated_text", "")
            if "Assistant:" in text:
                return text.split("Assistant:")[-1].strip()
            return text
        return "Sorry, I couldn't generate the itinerary. Please check your API token."
    except Exception as e:
        return f"Connection Error: {str(e)}"