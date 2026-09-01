# AI TEXT SUMMARIZER 

# Imports 
import os 
from dotenv import load_dotenv
from google import genai
from pathlib import Path 
import sys

# Get the API to create gemini client
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Summarize Function using our client
def summarize(text):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"Summarize this text and provide summarized, brief, concise simple text without stars etc in response. Just simple summarized text.\n\n{text}"
        )

        return response.text 

    except Exception as e:
        print(f"API ERROR: {e}")
        return None 

# Input and Output
print("==== ALI'S AI TEXT SUMMARIZER ====")
text = input("Enter Text to Summarize: \n")
if not text:
    print("Text can't be leaved empty.")
    sys.exit()
if text:
    summary = summarize(text)
print("==== SUMMARY ====")
print(summary)