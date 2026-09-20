# 🧠 NLP Toolkit

A simple NLP toolkit built with **Python, Hugging Face Transformers, Gemini API, and Streamlit**.

The project provides an interactive interface for experimenting with common NLP tasks, currently including **Sentiment Analysis** and **Question Answering**.

This project is part of my **AI Engineering learning journey**, where I’m building practical applications while learning how to integrate pretrained AI models and APIs into real-world applications.

---

## 🚀 Features

### 📊 Sentiment Analysis

* Uses Hugging Face's `pipeline()` for sentiment analysis.
* Analyzes multiple lines of text separately.
* Returns the predicted sentiment label and confidence score.
* Loads the model once using Streamlit Session State to avoid repeatedly initializing it during app interactions.

### ❓ Question Answering

* Uses Google's Gemini API to answer user questions.
* Generates short and direct answers.
* API credentials are loaded securely through environment variables.

### 🖥️ Interactive Streamlit Interface

* Task selection through a sidebar/radio interface.
* Separate input fields based on the selected NLP task.
* Loading indicators and basic error handling.
* Results displayed directly in the web application.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — Web application interface
* **Hugging Face Transformers** — Pretrained NLP models
* **Google Gemini API** — Question answering
* **python-dotenv** — Environment variable management

---

## 📁 Project Structure

```text
HuggingFace-NLP-Toolkit/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> **Note:** The `.env` file should never be committed to GitHub because it contains the Gemini API key.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/alirazasaleem-1/AI-Engineering-Projects.git
```

Navigate to the project directory:

```bash
cd AI-Engineering-Projects/02-Intermediate/03-HuggingFace-NLP-Toolkit
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

### 4. Configure the Gemini API

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 How It Works

### Sentiment Analysis

When the user selects **Sentiment Analysis**:

1. The user enters text.
2. The application loads the Hugging Face sentiment-analysis pipeline.
3. The model is stored in Streamlit Session State.
4. Each line of the input is analyzed separately.
5. The application displays the predicted sentiment and confidence score.

Example:

```text
Input:
I really enjoyed this product.

Output:
POSITIVE
Confidence: 99%+
```

### Question Answering

When the user selects **Question Answering**:

1. The user enters a question.
2. The question is sent to the Gemini API.
3. Gemini generates a brief answer.
4. The response is displayed in the Streamlit application.

---

## 🔐 Environment Variables

The project uses a `.env` file to keep API credentials outside the source code.

Required variable:

```env
GEMINI_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`:

```text
.env
.venv/
__pycache__/
```

---

## 🧠 What I Learned

This project helped me practice several practical AI Engineering concepts:

* Integrating pretrained Hugging Face models into applications
* Using the `transformers` pipeline API
* Working with external LLM APIs
* Managing API keys with environment variables
* Using Streamlit for AI application interfaces
* Using Session State to persist resources between interactions
* Handling user input and model errors
* Structuring an AI application around multiple tasks

---

## 🔄 Future Improvements

Planned improvements include:

* [ ] Named Entity Recognition (NER)
* [ ] Text Classification
* [ ] Better result formatting
* [ ] Confidence visualization
* [ ] Model selection
* [ ] Improved error handling
* [ ] Support for larger text inputs
* [ ] Evaluation using a small test dataset

---

## 🎯 Project Goal

The goal of this project is not just to use NLP models, but to understand how **AI models can be integrated into usable software applications**.

It is one step in my journey toward becoming an **AI Engineer** by building projects that combine models, APIs, Python, and application development.

---

## 👨‍💻 Author

**Ali Raza Saleem**

BS Computer Science Student | AI Engineering

GitHub: [alirazasaleem-1](https://github.com/alirazasaleem-1)

---

⭐ If you find this project useful, feel free to explore the repository and follow the journey.
