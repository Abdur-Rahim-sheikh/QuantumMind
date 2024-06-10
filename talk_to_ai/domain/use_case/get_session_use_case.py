from pydantic import BaseModel, InstanceOf
from ..models import Session
from ..repository import SessionRepository


class GetSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self, user_id: int, session_id: int) -> Session:
        return self.repository.get(user_id=user_id, session_id=session_id)
