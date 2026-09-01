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
def summarize(text, style):
    try:
        if style == "short":
            instruction = "Give a very short and concise summary."
        elif style == "detailed":
            instruction = "Give a detailed summary covering the important points."
        elif style == "bulletpoint":
            instruction = "Give a summary based on clear bulletpoints."

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"{instruction}.\n\n{text}"
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

    styles = ["short", "detailed", "bulletpoint"]
    style = input("Choose a summary style (short/detailed/bulletpoint): ")

    if style not in styles:
        print("Invalid Style Picked.")
        return 
    
    summary = summarize(text, style)
    print("\n==== SUMMARY ====")
    print(summary)

if __name__ == "__main__":
    main()
