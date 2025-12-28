import json
from config.settings import Settings

class Memory:
    def __init__(self):
        self.file = Settings.MEMORY_FILE
        self.data = self.load()

    def load(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self, role, message):
        self.data.append({"role": role, "message": message})
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)

    def history(self):
        return self.data