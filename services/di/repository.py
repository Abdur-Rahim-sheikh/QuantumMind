from ..domain.repository import ChatRepository
from ..data.repository import DefaultOllamaNoStream
from environs import Env

env = Env()
env.read_env()


class Repository:
    @property
    def chat_repository(self) -> ChatRepository:
        return DefaultOllamaNoStream(
            host=f"http://localhost:{env.str('OLLAMA_PORT')}",
        )
