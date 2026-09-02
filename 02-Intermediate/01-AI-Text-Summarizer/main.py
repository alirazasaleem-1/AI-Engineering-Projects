# AI TEXT SUMMARIZER 

# Imports 
import os 
import json 
from dotenv import load_dotenv
from google import genai
from pathlib import Path 
from datetime import datetime 

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
    
# File Read Function

def read_file(file_path):
    if file_path.exists():
        print("File exists.")
        with open(file_path, "r") as f:
            text = f.read() 
            return text 
    else:
        print("File doesn't exist.")
        return None 

# Log useful metadat Function
def log_metadata(input_type, style, text, success):
    metadata = {
        "input_type": input_type,
        "summary_style": style, 
        "text": text, 
        "success": success
    }

    log_file = Path("metadata.json")

    if log_file.exists():
        with open (log_file, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(metadata)

    with open (log_file, "w") as f:
        json.dump(logs, f, indent=4)
        

# Input and Output
def main():
    print("==== ALI'S AI TEXT SUMMARIZER ====")

    print("Type 1 for Text Input")
    print("Type 2 for File Input")
    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        text = input("Enter text to summarize: \n")
        
        if not text:
                print("Text can't be leaved empty. ")
                return  

        input_type == "text"

    elif choice == 2:
        file_path = Path(input("Ente the file Path: ").strip())
        text = read_file(file_path)

        if text is None:
            return

        input_type = "file"

    styles = ["short", "detailed", "bulletpoint"]
    style = input("Choose a summary style (short/detailed/bulletpoint): ")

    if style not in styles:
        print("Invalid Style Picked.")
        return 
    
    summary = summarize(text, style)
    if summary is None:
        log_metadata(input_type, style, text, False)
        return 
    
    print("\n==== SUMMARY ====")
    print(summary)

    log_metadata(input_type, style, text, True)

if __name__ == "__main__":
    main()
