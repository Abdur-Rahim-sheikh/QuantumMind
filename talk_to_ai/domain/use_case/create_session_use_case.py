from pydantic import BaseModel, InstanceOf

from ..models import Session
from ..repository import SessionRepository


class CreateSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self, user_id: int, session_name: str) -> Session:
        return self.repository.create(user_id=user_id, session_name=session_name)
