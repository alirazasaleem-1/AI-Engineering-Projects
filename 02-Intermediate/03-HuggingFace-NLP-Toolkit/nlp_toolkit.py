import streamlit as st 
from transformers import pipeline 
from google import genai 
import os
from pathlib import Path 
from dotenv import load_dotenv

# Loading env
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

# App Setup
st.set_page_config(page_icon="🧠", page_title="NLP Toolkit", layout="wide")
st.title("🧠 NLP Toolkit")

# Session State
if "loaded_model" not in st.session_state:
    st.session_state.loaded_model = None 

# Sidebar
with st.sidebar:
    st.header("📖 Instructions")
    st.markdown("""
**How to use:**
1. Select Task
2. Enter text to analyze or Question to get answer
3. Get results
""")

# Text Box
task = st.radio("Select Task", ["Sentiment Analysis", "Question Answering"])
text = ""
question = ""
if task == "Sentiment Analysis":
    text = st.text_area("Enter the text to analyze.", height=100)
if task == "Question Answering":
    question = st.text_area("Enter the Question to get answer.", height=150)
    response = client.models.generate_content(model="gemini-3.6-flash", contents = f"Answer this question briefly without saying anything else: {question}")
    st.write(response.text)

# Submit button
if st.button("Analyze"):
    if text:
        with st.spinner("🔃 Loading model..."):
            if st.session_state.loaded_model is None:
                st.session_state.loaded_model = pipeline("sentiment-analysis")

            model = st.session_state.loaded_model 
            sentences = text.split("\n")
            results = []
            try:
                for sentence in sentences:
                    result = model(sentence)
                    results.append(result)
                st.subheader("📊 Results")
                for i, result in enumerate(results):
                    st.write(f"{i+1}. {result}")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Sentiment", result[0]['label'])
                with col2:
                    st.metric("Confidence:", f"{result[0]['score']:.2%}")
            except Exception as e:
                st.error("❌ Error! Could not analyze. Try again.")
        
    else:
        st.warning("⚠ Please enter text first!")
