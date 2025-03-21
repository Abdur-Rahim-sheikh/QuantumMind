from pydantic import BaseModel

from ..models import Url
from ..repository import UrlShortenerRepository


class GetUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, long_url: str) -> Url:
        return self.repository.get(long_url=long_url)
