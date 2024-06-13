from abc import ABC, abstractmethod
from typing import Optional


class ChatRepository(ABC):
    @abstractmethod
    def generate(
        self,
        input_text: str,
        system: Optional[str],
    ) -> str:
        pass

    @abstractmethod
    def complete(self, chat_history: dict, context: str) -> str:
        pass

    @abstractmethod
    def generate_embeddings(self, text: str, model_name: str) -> list[float]:
        pass
