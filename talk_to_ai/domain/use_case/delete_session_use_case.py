from pydantic import BaseModel, InstanceOf
from ..repository import SessionRepository


class DeleteSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self, user_id: int, session_id: int) -> None:
        return self.repository.delete(user_id=user_id, session_id=session_id)
