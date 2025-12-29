# Jarvis AI – Personal AI Assistant (Gemini + OOP + Streamlit)

Jarvis AI একটি **Personal AI Assistant** যা Python দিয়ে তৈরি করা হয়েছে।
এটি ব্যবহারকারীর প্রশ্নের উত্তর দিতে পারে, শেখার সহায়তা করে, কোডিং ও ক্যারিয়ার গাইড দেয় এবং Gemini API ব্যবহার করে বুদ্ধিমান রেসপন্স তৈরি করে।

এই প্রজেক্টটি সম্পূর্ণভাবে **Object-Oriented Programming (OOP)** অনুসরণ করে তৈরি করা হয়েছে এবং **Streamlit UI** ব্যবহার করা হয়েছে।

---

## Features

### Basic Interaction
- User greeting (Personal assistant style)
- Text-based conversation
- Streamlit interactive UI

### Smart Assistance
- General question answering
- Tutor mode (learning support)
- Coding assistant
- Career guidance helper

### Generative AI (Gemini)
- Uses **Google Gemini API**
- Intelligent responses using LLM
- System-level instruction control
- Graceful error handling

### Memory System
- Conversation memory stored in JSON
- Previous chats are remembered
- Context-aware responses

---

## Core Components

- **Gemini Engine** → Handles Gemini API communication  
- **Assistant Brain** → Main logic controller  
- **Prompt Controller** → System behavior & roles  
- **Memory Manager** → JSON-based conversation memory  
- **Streamlit UI** → User interaction interface  

---

## Project Structure

jarvis_assistant/
│
├── app.py # Streamlit UI
├── .env # API key
├── requirements.txt
├── list_models.py # Check supported Gemini models
│
├── config/
│ └── settings.py # Environment & config
│
├── jarvis/
│ ├── assistant.py # JARVIS brain
│ ├── gemini_engine.py # Gemini API handler
│ ├── prompt_controller.py# System instructions
│ └── memory.py # Conversation memory
└── README.md

## Setup

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate

Install Required Libraries

pip install -r requirements.txt
pip install --upgrade google-generativeai

Add API Key:

Create a .env file:
GEMINI_API_KEY=My_GEMINI_API_KEY

Supported Model:
models/gemini-2.5-flash

Update in config/settings.py:
MODEL_NAME = "models/gemini-2.5-flash"

Run Project:
streamlit run app.py

Tech Used:

Python 3.10+
Streamlit
google-generativeai
python-dotenv
JSON (memory storage)

👤 Author
Md Mahabub Alam Bishal
Diploma in Computer Science
Inspired by Boktiar Ahmed Bappy