from pydantic import BaseModel

from ..repository import UrlShortenerRepository


class DeleteUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, short_url: str):
        return self.repository.delete(short_url=short_url)
