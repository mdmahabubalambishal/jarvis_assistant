class PromptController:
    def system_prompt(self, role):
        base_prompt = (
            "You are JARVIS, a smart, polite, helpful personal AI assistant.\n"
        )

        role_prompt = {
            "Tutor": "Act as a tutor. Explain step by step with examples.\n",
            "Coder": "Act as a coding assistant. Write clean Python code.\n",
            "Career": "Act as a career advisor. Give career guidance.\n",
            "General": ""
        }

        return base_prompt + role_prompt.get(role, "")