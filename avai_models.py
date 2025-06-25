import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List available models
print("✅ Available models:")
for model in genai.list_models():
    print("-", model.name)
