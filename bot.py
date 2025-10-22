# main.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # by default looks for a .env file in cwd

# Read the API key from the environment
API_KEY = os.getenv("G_API_KEY")

if not API_KEY:
    raise RuntimeError("GENAI_API_KEY not found. Put it in a .env file or set it in your environment.")

# Create the client
client = genai.Client(api_key=API_KEY)

# Example loop
while True:
    print("-" * 70)
    userInput = input("Ask anything: -> ").strip()
    if userInput.lower() in ("exit", "break"):
        break

    res = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=userInput
    )
    print("Bot ->", getattr(res, "text", res))
