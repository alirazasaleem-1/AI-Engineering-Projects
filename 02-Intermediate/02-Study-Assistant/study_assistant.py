import streamlit as st
import  google.generativeai as  genai 
from dotenv import load_dotenv
from pathlib import Path 
import os 

# Loading env
env_path = Path(__name__).parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.6-flash")


# App Setup
st.set_page_config(page_icon="🏫", page_title="AI Study Assistant", layout="wide")
st.title("📚 AI Study Assistant")

# Session State 
if "notes" not in st.session_state:
    st.session_state.notes = ""
if "history" not in st.session_state:
    st.session_state.history = []

# Side Bar 
with st.sidebar:
    st.header("📖 Instructions")
    st.markdown("""
    **How to use:**
    1. Upload / Paste notes
    2. Ask questions
    3. Get answers
    """)

# User choice: File upload ya Type notes?
input_method = st.radio("Choose input method: ", ["Upload File", "Type Notes"])

if input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload (.txt)")

    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        st.session_state.notes = content 
        st.success("✅ Notes Loaded.")
else:
    notes_text = st.text_area("Paste notes: ")

    if notes_text:
        st.session_state.notes = notes_text
        st.success("✅ Notes Saved.")

# Question input 
question = st.text_input("Your question: ")
if st.button("Submit Question"):

    if question:
        st.session_state.history.append({
            "question": question,
            "answer": "Pending response..."
        })
        st.success(f"✅ {question}")
    else:
        st.warning("⚠ Please enter a question.")

# Displaying Questions
if st.session_state.history:
    for i, item in enumerate(st.session_state.history):
        st.write(f"**Q{i+1}:** {item['question']}")
        st.write(f"**A:** {item['answer']}")
        st.divider()
else:
    st.info("💡 No questions asked yet. Ask your first question! ")