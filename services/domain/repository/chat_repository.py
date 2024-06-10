from abc import ABC, abstractmethod


class ChatRepository(ABC):
    @abstractmethod
    def generate(self, input_text: str) -> str:
        pass

    @abstractmethod
    def complete(self, chat_history: list[str], context: str) -> str:
        pass

    @abstractmethod
    def generate_embeddings(self, text: str, model_name: str) -> list[float]:
        pass
