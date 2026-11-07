import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key is missing. Check your .env file.")
    exit()

# Connect to Gemini
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")

# Ask Gemini a question
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Python virtual environments in two simple sentences."
)

# Display answer
print("\nGemini says:")
print(response.text)

client.close()