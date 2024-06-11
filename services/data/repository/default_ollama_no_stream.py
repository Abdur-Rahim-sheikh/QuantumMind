import logging
from typing import Optional
import ollama
from ollama import Client

from services.domain.repository import ChatRepository

logger = logging.getLogger(__name__)


class DefaultOllamaNoStream(ChatRepository):
    def __init__(self, host: str, model: str = "gemma:2b"):
        self.host = host
        self.model = model
        self.client = Client(host=host)

    def set_model(self, model: str) -> None:
        self.model = model

    def generate(self, input_text: str) -> str:
        # try:
        logger.debug(
            f"{self.client.generate(model=self.model, prompt=input_text, stream=False)=}"
        )
        response = self.client.generate(
            model=self.model, prompt=input_text, stream=False
        )
        # except (ollama.RequestError, ollama.ResponseError) as e:
        #     raise RuntimeError(f"Could not generate ai chat: {e}")
        return response["response"]

    def complete(self, chat_history: list[str], context: str) -> str:
        messages = []
        for i, message in enumerate(chat_history):
            role = "user" if i % 2 == 0 else "assistant"
            messages.append({"role": role, "content": message})

        messages.append({"role": "user", "content": context})
        try:

            response = self.client.chat(
                model=self.model, messages=messages, stream=False
            )
        except (ollama.RequestError, ollama.ResponseError) as e:
            raise RuntimeError(f"Could not complete ai chat: {e}")
        return response["message"]["content"]

    def create_model(self, model_name: str, parameters: dict) -> str:
        pass

    def list_local_models(self) -> list[dict]:
        try:
            response = self.client.list()
        except (ollama.RequestError, ollama.ResponseError) as e:
            raise RuntimeError(f"Could not list local models: {e}")
        return response["models"]

    def show_model_information(self, model_name: Optional[str]) -> dict:
        if not model_name:
            model_name = self.model
        try:
            response = self.client.show(model=model_name)
        except (ollama.RequestError, ollama.ResponseError) as e:
            raise RuntimeError(f"Could not show model information: {e}")
        return response

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
