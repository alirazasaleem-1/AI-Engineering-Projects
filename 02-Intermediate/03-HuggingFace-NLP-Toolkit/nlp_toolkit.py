import streamlit as st 
from transformers import pipeline 

# App Setup
st.set_page_config(page_icon="🧠", page_title="NLP Toolkit", layout="wide")
st.title("🧠 Hugging Face NLP Toolkit")

# Session State
if "loaded_model" not in st.session_state:
    st.session_state.loaded_model = None 
if "current_task" not in st.session_state:
    st.session_state.current_task = None 

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
task = st.selectbox("Choose Task:", ["Sentiment Analysis", "Text Classification", "Named Entity Recognition"])
st.write(f"Selected Task: {task}")

# Text Box
st.subheader("Enter Text to Analyze")
text = st.text_area("Paste your text here:", height=100)

# Submit button
if st.button("Analyze"):
    if text:
        st.write("Processing...")

        if task != st.session_state.current_task:
            st.session_state.loaded_model = None
            st.session_state.current_task = task 

        if task == "Sentiment Analysis":
            if st.session_state.loaded_model is None:
                st.session_state.loaded_model = pipeline("sentiment-analysis")
        elif task == "Text Classification":
            if st.session_state.loaded_model is None:
                st.session_state.loaded_model = pipeline("zero-shot-classification")
        elif task == "Named Entity Recognition":
            if st.session_state.loaded_model is None:
                st.session_state.loaded_model = pipeline("ner")

        model = st.session_state.loaded_model 
        try:
            result = model(text)
            st.subheader("📊 Results")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Sentiment", result[0]['label'])
            with col2:
                st.metric("Confidence:", f"{result[0]['score']:.2%}")
        except Exception as e:
            st.error("❌ Error! Could not analyze. Try again.")
        
    else:
        st.warning("⚠ Please enter text first!")
