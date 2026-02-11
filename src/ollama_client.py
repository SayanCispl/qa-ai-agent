"""
Ollama Client Module
--------------------
Responsible for:
- Connecting to local Ollama server
- Sending prompts to LLM
- Returning generated response
"""

import requests

class OllamaClient:
    def __init__(self, model="llama3"):
        """
                Initialize Ollama connection.

                :param model: Name of local model (e.g., llama3, mistral)
                """
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt, max_tokens=1000):
        """
                Send prompt to Ollama and get response.

                :param prompt: Text prompt
                :param max_tokens: Limit generation size
                :return: Generated text
                """

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens
            }
        }
        # Send POST request to Ollama server
        response = requests.post(self.url, json=payload, timeout=300)
        # Raise error if server fails
        response.raise_for_status()

        return response.json()["response"]
