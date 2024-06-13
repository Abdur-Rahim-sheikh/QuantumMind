from .repository import Repository
from ..domain.use_case import (
    GetAllSessionUseCase,
    CreateSessionUseCase,
    GetSessionUseCase,
    UpdateSessionUseCase,
    DeleteSessionUseCase,
    ExistsSessionUseCase,
)


class UseCase:
    def __init__(self):
        self.__repository = Repository()

    @property
    def get_all_sessions(self) -> GetAllSessionUseCase:
        return GetAllSessionUseCase(repository=self.__repository.session_repository)

    @property
    def create_session(self) -> CreateSessionUseCase:
        return CreateSessionUseCase(repository=self.__repository.session_repository)

    @property
    def get_session(self) -> GetSessionUseCase:
        return GetSessionUseCase(repository=self.__repository.session_repository)

    @property
    def update_session(self) -> UpdateSessionUseCase:
        return UpdateSessionUseCase(repository=self.__repository.session_repository)

    @property
    def delete_session(self) -> DeleteSessionUseCase:
        return DeleteSessionUseCase(repository=self.__repository.session_repository)

    @property
    def exists_session(self) -> ExistsSessionUseCase:
        return ExistsSessionUseCase(repository=self.__repository.session_repository)
