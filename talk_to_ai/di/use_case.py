from .repository import Repository
from ..domain.use_case import GetAllSessionUseCase


class UseCase:
    def __init__(self):
        self.__repository = Repository()

    @property
    def get_all_sessions(self) -> GetAllSessionUseCase:
        return GetAllSessionUseCase(repository=self.__repository.session_repository)
