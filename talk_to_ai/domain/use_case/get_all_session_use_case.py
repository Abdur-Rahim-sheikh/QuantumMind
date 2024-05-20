from pydantic import BaseModel, InstanceOf

from ..models import Session
from ..repository import SessionRepository


class GetAllSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self, user_id: int) -> list[Session]:
        return self.repository.get_all(user_id=user_id)
