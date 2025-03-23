from ..models import Url
from ..repository import UrlShortenerRepository


class GetAllUrlsUseCase:
    def __init__(self, repository: UrlShortenerRepository):
        self.repository = repository

    def __call__(self) -> list[Url]:
        return self.repository.get_all()
