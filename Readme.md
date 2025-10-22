# Gemini Chat CLI

A simple **command-line chatbot** built with Google’s **Gemini API (via the `google-genai` library)**.  
This project allows you to interact with the Gemini model directly from your terminal.

---

## 🚀 Features
- Chat interactively with the **Gemini 2.5 Flash** model  
- Supports dynamic input/output in the console  
- Uses environment variables for secure API key management  
- Clean, minimal Python implementation

---

## 🧩 Requirements
- Python 3.9 or later  
- A valid [Google AI Studio API key](https://aistudio.google.com/app/apikey)  
- The following Python packages:
  ```bash
  pip install python-dotenv google-genai

## create .env file
- G_API_KEY=your_google_api_key_here


## run the script 
  python main.py
