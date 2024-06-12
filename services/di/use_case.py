from .repository import Repository
from ..domain.use_case import ChatGenerateUseCase


class ServiceUseCase:
    def __init__(self):
        self.__repository = Repository()

    @property
    def chat_generate_use_case(self) -> ChatGenerateUseCase:
        return ChatGenerateUseCase(chat_repository=self.__repository.chat_repository)
