from abc import ABC, abstractmethod

from ..models import Session


class SessionRepository(ABC):
    @abstractmethod
    def create(self, user_id: int, session_name: str):
        pass

    @abstractmethod
    def get(self, user_id: int, session_id: int) -> Session:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[Session]:
        pass

    @abstractmethod
    def update(self, user_id: int, session: Session):
        pass

    @abstractmethod
    def delete(self, user_id: int, session_id: int):
        pass
