from pydantic import BaseModel, InstanceOf
from ..repository import SessionRepository


class ExistsSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self, user_id: int, session_id: int) -> bool:
        return self.repository.exists(user_id, session_id)
