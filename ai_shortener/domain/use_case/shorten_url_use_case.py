import base64

from ..repository import UrlShortenerRepository


class ShortenUrlUseCase:
    def __init__(self, repository: UrlShortenerRepository):
        self.repository = repository

    def __call__(self, long_url: str, title: str = None, description: str = None, img: base64 = None):
        return self.repository.shorten(long_url=long_url, title=title, description=description, img=img)
