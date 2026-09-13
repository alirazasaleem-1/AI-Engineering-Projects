import streamlit as st 
from transformers import pipeline 

# App Setup
st.set_page_config(page_icon="🧠", page_title="NLP Toolkit", layout="wide")
st.title("🧠 Hugging Face NLP Toolkit")

# Sidebar
with st.sidebar:
    st.header("📖 Instructions")
    st.markdown("""
**How to use:**
1. Select NLP Task (Sentiment, Classification, etc)
2. Enter text to analyze
3. Get results
""")