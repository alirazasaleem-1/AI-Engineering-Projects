import streamlit as st 

st.title("📚 AI Study Assistant")

# File Uploader
uploaded_file = st.file_uploader("Upload notes (.txt)")

# Text Input
question = st.text_input("Your question: ")

# Button
if st.button("Ask"):
    st.write(f"Notes loaded: {uploaded_file}")
    st.write(f"Question: {question}")
