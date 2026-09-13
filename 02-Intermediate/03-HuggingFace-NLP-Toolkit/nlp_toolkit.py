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

# Select Box
st.subheader("Select NLP Task")
task = st.selectbox("Choose Task:", ["Sentiment Analysis", "Text Classification", "Question Answering", "Named Entity Recognition"])
st.write(f"Selected Task: {task}")

# Text Box
st.subheader("Enter Text to Analyze")
text = st.text_area("Paste your text here:", height=100)

# Submit button
if st.button("Analyze"):
    if text:
        st.write("Processing...")
    else:
        st.warning("⚠ Please enter text first!")
