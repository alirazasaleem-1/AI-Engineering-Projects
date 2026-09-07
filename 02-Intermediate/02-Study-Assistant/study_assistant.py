import streamlit as st

# App Setup
st.set_page_config(page_icon="🏫", page_title="AI Study Assistant", layout="wide")
st.title("📚 AI Study Assistant")

# Session State 
if "notes" not in st.session_state:
    st.session_state.notes = ""

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
else:
    notes_text = st.text_area("Paste notes: ")

# Question input 
question = st.text_input("Your question: ")
if st.button("Submit Question"):
    st.success(f"✅ {question}")