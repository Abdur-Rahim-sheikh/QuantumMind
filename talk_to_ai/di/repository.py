from ..domain.repository import SessionRepository
from ..data.repository import DefaultSessionRepository


class Repository:
    @property
    def session_repository(self) -> SessionRepository:
        return DefaultSessionRepository()
