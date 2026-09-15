import streamlit as st 
from transformers import pipeline 

# App Setup
st.set_page_config(page_icon="🧠", page_title="NLP Toolkit", layout="wide")
st.title("🧠 Hugging Face NLP Toolkit")

# Session State
if "loaded_model" not in st.session_state:
    st.session_state.loaded_model = None 

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

        if task == "Sentiment Analysis":
            model = pipeline("sentiment-analysis")
        elif task == "Text Classification":
            model = pipeline("zero-shot-classification")
        elif task == "Question Answering":
            model = pipeline("question-answering")
        elif task == "Named Entity Recognition":
            model = pipeline("ner")

        st.session_state.loaded_model = model 
        result = model(text)
        st.subheader("📊 Results")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sentiment", f"result[0]['label']")
        with col2:
            st.metric("Confidence:", f"{result[0]['score']:.2%}")
    else:
        st.warning("⚠ Please enter text first!")
