from pydantic import BaseModel

from ..repository import UrlShortenerRepository


class DeleteUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, pid: int):
        return self.repository.delete(pid=pid)
