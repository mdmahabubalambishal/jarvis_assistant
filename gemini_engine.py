import google.generativeai as genai
from config.settings import Settings

class GeminiEngine:
    def __init__(self):
        genai.configure(api_key=Settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Settings.MODEL_NAME)

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"