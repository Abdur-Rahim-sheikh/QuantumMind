from pydantic import BaseModel, InstanceOf

from ..models import Session
from ..repository import SessionRepository


class UpdateSessionUseCase(BaseModel):
    repository: InstanceOf[SessionRepository]

    def __call__(self, session: Session) -> None:
        return self.repository.update(session)
