import streamlit as st

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