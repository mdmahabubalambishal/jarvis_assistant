import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "models/gemini-2.5-flash"
    MEMORY_FILE = "conversation_memory.json"