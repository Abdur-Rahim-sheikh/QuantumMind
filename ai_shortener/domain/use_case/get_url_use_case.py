from typing import Optional

from pydantic import BaseModel

from ..models import Url
from ..repository import UrlShortenerRepository


class GetUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, pid: int) -> Optional[Url]:
        return self.repository.get(pid=pid)
