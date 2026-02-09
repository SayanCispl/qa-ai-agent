import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def ask_llm(system_prompt: str, user_prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": f"{system_prompt}\n\n{user_prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
