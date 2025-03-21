from pydantic import BaseModel

from ..models import Url
from ..repository import UrlShortenerRepository


class GetAllUrlsUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self) -> list[Url]:
        return self.repository.get_all()
