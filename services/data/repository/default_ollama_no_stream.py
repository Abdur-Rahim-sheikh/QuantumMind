from typing import Optional

from services.domain.repository import ChatRepository
import requests


class DefaultOllamaNoStream(ChatRepository):
    def __init__(self, host: str, model: str = "llama3"):
        self.host = host
        self.model = model

    def setModel(self, model: str) -> None:
        self.model = model

    def generate(self, input_text: str) -> str:
        url = f"{self.host}/api/generate"
        data = {"model": self.model, "prompt": input_text, "stream": False}
        response = requests.post(url, json=data)
        return response.json()["response"]

    def complete(self, chat_history: list[str], context: str) -> str:
        url = f"{self.host}/api/chat"
        messages = []
        for idx, message in enumerate(chat_history):
            role = "assistant" if (idx & 1) else "user"
            messages.append({"role": role, "content": message})
        messages.append({"role": "user", "content": context})
        data = {"model": self.model, "messages": messages}
        try:
            response = requests.post(url, json=data)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Could not ask the question: {e}")
        return response.json()["response"]

    def create_model(self, model_name: str, parameters: dict) -> str:
        pass

    def list_local_models(self) -> list[dict]:
        url = f"{self.host}/api/models"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Could not list local models: {e}")
        return response.json()["models"]

    def show_model_information(self, model_name: Optional[str]) -> dict:
        if not model_name:
            model_name = self.model
        url = f"{self.host}/api/show"
        data = {"name": model_name}
        try:
            response = requests.post(url, json=data)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Could not show model information: {e}")
        return response.json()

    def copy_model(self, source_model: str, destination_model: str) -> str:
        pass

    def delete_model(self, model_name: str) -> str:
        pass

    def pull_model(self, model_name: str, remote_url: str) -> str:
        pass

    def push_model(self, model_name: str, remote_url: str) -> str:
        pass

    def generate_embeddings(self, text: str, model_name: str) -> list[float]:
        pass

    def list_running_models(self) -> list[str]:
        pass
