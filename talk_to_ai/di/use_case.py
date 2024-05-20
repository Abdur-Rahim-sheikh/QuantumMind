from .repository import Repository
from ..domain.use_case import GetAllSessionUseCase


class UseCase:
    def __init__(self):
        self.__repository = Repository()

    def get_all_session_use_case(self):
        return GetAllSessionUseCase(repository=self.__repository.session_repository)
