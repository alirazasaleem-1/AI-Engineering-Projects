# 📚 AI Study Assistant

An AI-powered study assistant that helps students understand their own study notes through natural-language questions. The application uses Google's Gemini API to generate concise, context-aware answers while maintaining conversation history within the active session.

Built as **Project 5** in my AI Engineering project-based curriculum, this project focuses on integrating a generative AI API into a user-facing application while applying practical software engineering fundamentals such as state management, input validation, error handling, environment-based configuration, and prompt guardrails.

---

## 🚀 Features

- 📄 Upload `.txt` study notes
- ✍️ Paste notes directly into the application
- 💬 Ask natural-language questions about the notes
- 🤖 Generate AI-powered answers using Gemini
- 🧠 Maintain conversation history during the session
- 🛡️ Keep API credentials outside the source code
- ⚠️ Validate missing notes and questions
- 🔧 Handle API/runtime failures gracefully
- 🎨 Clean and simple Streamlit interface

---

## 🏗️ Application Architecture

```text
User
 │
 ├── Upload Notes
 │
 └── Paste Notes
        │
        ▼
┌─────────────────────┐
│   Session State     │
│  Notes + History    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Prompt Construction │
│ + System Guardrails │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Gemini API      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Generated Answer  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Conversation History│
└─────────────────────┘
````

---

## 🧰 Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Application logic               |
| Streamlit         | Web application UI              |
| Google Gemini API | AI-powered response generation  |
| python-dotenv     | Environment variable management |
| pathlib           | File/path handling              |
| Git & GitHub      | Version control                 |

---

## 🧠 Key Engineering Concepts

### 1. AI API Integration

Integrated Google's Gemini API to transform user questions and study notes into context-aware AI responses.

### 2. Prompt Engineering

Implemented system instructions to guide the model toward:

* Staying focused on the provided notes
* Giving short and understandable answers
* Avoiding unrelated questions
* Behaving as a student-focused assistant

### 3. Session State Management

Used Streamlit's session state to preserve:

* Loaded study notes
* Conversation history
* User interactions across Streamlit reruns

### 4. Input Validation

The application checks for:

* Missing study notes
* Empty questions
* Invalid user input

This prevents unnecessary API calls and improves the user experience.

### 5. Error Handling

External API calls are wrapped with exception handling so unexpected failures don't crash the application.

### 6. Secure Configuration

The Gemini API key is loaded from an environment variable instead of being hardcoded into the source code.

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should never be committed to Git.

---

## 📂 Project Structure

```text
AI-Study-Assistant/
│
├── study_assistant.py
├── README.md
├── .env
├── .gitignore
└── requirements.txt
```

> `.env` should be excluded from version control through `.gitignore`.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/alirazasaleem-1/AI-Engineering-Projects.git
cd AI-Engineering-Projects/02-Intermediate/01-AI-Study-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run study_assistant.py
```

The application will open in your browser.

---

## 💡 Example Workflow

```text
1. Launch the application
        ↓
2. Upload or paste study notes
        ↓
3. Enter a question
        ↓
4. Application builds a contextual prompt
        ↓
5. Gemini generates an answer
        ↓
6. Question + answer are added to session history
        ↓
7. Continue asking questions
```

---

## 🛡️ Error Handling

The application handles common failure scenarios including:

* No notes provided
* No question provided
* Gemini API failures
* Unexpected runtime exceptions

Instead of exposing technical errors directly to users, the application provides simple feedback and allows them to try again.

---

## 🔐 Security Considerations

API credentials are managed through environment variables.

```python
api_key = os.getenv("GEMINI_API_KEY")
```

Sensitive configuration is intentionally separated from application source code.

The repository should contain:

```text
.env.example
```

instead of the real `.env` file when sharing the project publicly.

---

## 📈 Development Process

The project was developed incrementally through four milestones:

### Milestone 1 — UI Foundation

* Streamlit page configuration
* Sidebar instructions
* Notes input
* Question input
* Basic interaction flow

### Milestone 2 — State Management

* Session state initialization
* Persistent notes
* Conversation history
* File content storage

### Milestone 3 — AI Integration

* Gemini API configuration
* Environment-based API key
* System instructions
* Prompt construction
* AI response generation

### Milestone 4 — Reliability

* Input validation
* Exception handling
* User-friendly error messages
* Edge-case handling

This incremental approach made it easier to test each layer before adding the next one.

---

## 📝 Git Workflow

The project was developed using incremental commits rather than one large final commit:

```text
feat: Milestone 1 - UI Setup
feat: Milestone 2 - Session State Management
feat: Milestone 3 - Gemini API Integration
feat: Milestone 4 - Error Handling & Edge Cases
```

This reflects a structured development workflow where individual features are implemented and verified progressively.

---

## 📊 Project Stats

| Metric           |     Result |
| ---------------- | ---------: |
| Development Time | ~6–7 hours |
| Milestones       |          4 |
| Main Application | ~150 lines |
| AI APIs          |          1 |
| Input Methods    |          2 |
| Core Features    |         8+ |
| Git Commits      |          4 |

---

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* Python application development
* Streamlit
* Generative AI APIs
* Gemini API integration
* Prompt engineering
* System instructions and guardrails
* Session state
* File I/O
* Environment variables
* API security fundamentals
* Input validation
* Exception handling
* Git-based development

More importantly, it demonstrates the ability to move from **AI concepts to a working user-facing application**.

---

## 🔮 Future Improvements

Potential next iterations could include:

* 📑 Support for PDF and DOCX notes
* 🧠 Persistent conversation storage
* 📝 Automatic note summarization
* 🎴 Flashcard generation
* ❓ Automatic quiz generation
* 🔎 Retrieval-based question answering
* 📊 Study progress tracking
* 👤 User authentication
* 🚀 Cloud deployment

These improvements would gradually move the project from a simple AI application toward a more complete AI study platform.

---

## 🚀 Project Roadmap

This project is part of my broader journey toward becoming a practical AI Engineer.

```text
Python Foundations
       ↓
APIs & Data Handling
       ↓
Generative AI Applications
       ↓
AI Study Assistant  ← You are here
       ↓
Hugging Face & NLP
       ↓
RAG Applications
       ↓
AI + SQL
       ↓
AI Agents
       ↓
Production AI Systems
```

---

## 👨‍💻 Author

**Ali Raza Saleem**

BS Computer Science Student | Aspiring AI Engineer

Building practical AI projects with Python and documenting the journey through GitHub..

---

## 🎯 Key Takeaway

| Focus                   | What I Learned                                                                |
| ----------------------- | ----------------------------------------------------------------------------- |
| **AI Integration**      | Built a real AI application using the Gemini API                              |
| **Prompt Engineering**  | Designed instructions and guardrails for focused responses                    |
| **State Management**    | Preserved notes and conversation history with Streamlit session state         |
| **Reliability**         | Added input validation and graceful error handling                            |
| **Security**            | Managed API credentials through environment variables                         |
| **Engineering Mindset** | Learned that building AI products requires more than just calling an AI model |

**The key lesson:** Building AI applications is not just about the model — it’s about building everything around it to make the system **usable, reliable, and secure.** 🚀