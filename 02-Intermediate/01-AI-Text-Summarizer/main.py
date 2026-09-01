# AI TEXT SUMMARIZER 

# Imports 
import os 
from dotenv import load_dotenv
from google import genai
from pathlib import Path 

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
def main():
    print("==== ALI'S AI TEXT SUMMARIZER ====")

    text = input("Enter text to summarize: \n")
    if not text:
        print("Text can't be leaved empty. ")
        return  
    summary = summarize(text)
    print("\n==== SUMMARY ====")
    print(summary)

if __name__ == "__main__":
    main()
