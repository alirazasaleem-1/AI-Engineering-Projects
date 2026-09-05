# 🤖 AI Text Summarizer

A Python-based AI Text Summarizer that uses Google's Gemini API to generate summaries in different styles. The application accepts either directly pasted text or text files and allows the user to choose between short, detailed, and bullet-point summaries.

## 🚀 Features

- Summarize text using Google's Gemini API
- Three summary styles:
  - Short
  - Detailed
  - Bullet-point
- Accept text directly from the user
- Accept text from a `.txt` file
- Validate empty text input
- Handle missing files
- Handle API errors
- Keep API keys secure using environment variables
- Log useful non-sensitive metadata in JSON format
- Simple command-line interface

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- pathlib
- JSON

## 📁 Project Structure

```text
AI-Text-Summarizer/
├── main.py
├── .env
├── .gitignore
├── metadata.json
└── README.md
```

## 🔐 API Key Setup

The Gemini API key is stored in an environment variable instead of being written directly in the source code.

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should not be committed to GitHub. Add it to `.gitignore`:

```text
.env
```

## 📦 Installation

Install the required packages:

```bash
pip install google-genai python-dotenv
```

## ▶️ How to Run

Run the Python file:

```bash
python main.py
```

The application will ask whether you want to provide text input or file input. You can then choose one of the available summary styles:

```text
short
detailed
bulletpoint
```

## 🧠 How It Works

The application follows this basic workflow:

User Input → Text/File → Input Validation → Summary Style → Prompt → Gemini API → Generated Summary → Metadata Logging

The `summarize()` function receives the text and selected style, creates an instruction based on the selected style, and sends the request to the Gemini model.

## ✍️ Summary Styles

### Short

Produces a very concise summary containing the main idea.

### Detailed

Produces a detailed summary covering the important points from the input.

### Bullet-point

Produces the summary using clear bullet points.

## 📝 Prompt Approach

The application changes the instruction depending on the selected summary style.

Examples of the instructions used:

- Short: "Give a very short and concise summary."
- Detailed: "Give a detailed summary covering the important points."
- Bullet-point: "Give a summary based on clear bullet points."

The selected instruction is combined with the user's text and sent to the Gemini model.

## 📊 Metadata Logging

The application logs useful non-sensitive information about each summarization request in `metadata.json`.

The metadata can include information such as:

- Input type
- Summary style
- Input length
- Success status
- Timestamp

The original input text is not stored in the metadata log.

This provides basic information about application usage without unnecessarily storing the user's original content.

## 🛡️ Error Handling

The application handles several common problems:

- Empty text input
- File that does not exist
- Invalid summary style
- API errors

API errors are caught using exception handling so the application can fail gracefully instead of unexpectedly crashing.

## ⚠️ Limitations

This project was built as an intermediate learning project, so it intentionally keeps the architecture simple.

Current limitations include:

- Command-line interface only
- No graphical user interface
- No database
- No advanced retry mechanism
- No token or cost tracking
- No automated evaluation system
- Text files are the primary supported file format
- Summary quality depends on the selected Gemini model and prompt

## 🎯 Learning Objectives

This project was built to practice:

- Working with an LLM API
- Using API keys securely
- Environment variables
- Python SDKs
- Prompt construction
- Reusable functions
- File handling
- JSON data handling
- Exception handling
- Metadata logging
- Building an AI-powered application from scratch

## 🔮 Possible Future Improvements

Possible future improvements include:

- Streamlit web interface
- Support for additional file formats
- More advanced prompt templates
- Token and cost tracking
- Retry and timeout handling
- Automated evaluation
- Additional summary styles
- Structured outputs
- Prompt injection protection

## 👨‍💻 Author

**Ali Raza**

BS Computer Science Student | Python & AI Engineering Learner

This project is part of my journey toward becoming an AI Engineer and building practical AI-powered applications.

## 📌 Project Status

**Completed ✅**

The project demonstrates the fundamentals of building an LLM-powered Python application that accepts text or file input, generates controlled summaries using Gemini, handles common errors, protects API credentials, and records useful non-sensitive metadata... 