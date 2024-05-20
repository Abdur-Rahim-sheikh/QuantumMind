from pydantic import BaseModel, InstanceOf

from ..models import Session
from ..repository import SessionRepository


class GetAllSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self) -> list[Session]:
        return self.repository.get_all()
