import requests


class OllamaClient:
    def __init__(self, model="llama3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt, max_tokens=1000):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens
            }
        }

        response = requests.post(self.url, json=payload, timeout=300)
        response.raise_for_status()

        return response.json()["response"]
