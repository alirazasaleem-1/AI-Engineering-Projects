import streamlit as st 
from transformers import pipeline 

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
1. Analyze sentiment of your text
2. Enter text to analyze
3. Get results
""")

# Text Box
st.subheader("Enter Text to Analyze")
text = st.text_area("Paste your text here:", height=150)

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
                    result = model(text)
                    results.append(result)
                st.subheader("📊 Results")
                for i, result in enumerate(results):
                    print(f"{i+1}. {result}")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Sentiment", result[0]['label'])
                with col2:
                    st.metric("Confidence:", f"{result[0]['score']:.2%}")
            except Exception as e:
                st.error("❌ Error! Could not analyze. Try again.")
        
    else:
        st.warning("⚠ Please enter text first!")
