from ..data.repository import DefaultUrlShortenerRepository
from ..domain.repository import UrlShortenerRepository


class Repository:
    @property
    def url_repository(self) -> UrlShortenerRepository:
        return DefaultUrlShortenerRepository()
