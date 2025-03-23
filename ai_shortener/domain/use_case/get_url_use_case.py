from typing import Optional

from ..models import Url
from ..repository import UrlShortenerRepository


class GetUrlUseCase:
    def __init__(self, repository: UrlShortenerRepository):
        self.repository = repository

    def __call__(self, pid: int) -> Optional[Url]:
        return self.repository.get(pid=pid)
