from jarvis.gemini_engine import GeminiEngine
from jarvis.prompt_controller import PromptController
from jarvis.memory import Memory

class JarvisAssistant:
    def __init__(self):
        self.gemini = GeminiEngine()
        self.prompt = PromptController()
        self.memory = Memory()

    def greet(self):
        return "Hello! I am JARVIS, your personal AI assistant."

    def chat(self, user_input, role):
        system_prompt = self.prompt.system_prompt(role)
        history = self.memory.history()

        conversation = system_prompt
        for msg in history[-5:]:
            conversation += f"{msg['role']}: {msg['message']}\n"

        conversation += f"User: {user_input}"

        response = self.gemini.generate_response(conversation)

        self.memory.save("User", user_input)
        self.memory.save("JARVIS", response)

        return response