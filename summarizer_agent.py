import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key is set
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Load the model
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

# Prompt user for a file path
file_path = input("Enter the path to your .txt file: ").strip('"')

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    prompt = f"Summarize the following text:\n\n{text}"

    # Generate summary
    response = model.generate_content(prompt)

    print("\nSummary\n")
    print(response.text)

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
