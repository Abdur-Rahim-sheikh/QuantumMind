from .repository import Repository
from ..domain.use_case import ChatGenerateUseCase


class UseCase:
    def __init__(self):
        self.__repository = Repository()

    def generate_chat_use_case(self) -> ChatGenerateUseCase:
        return ChatGenerateUseCase(chat_repository=self.__repository.chat_repository)
