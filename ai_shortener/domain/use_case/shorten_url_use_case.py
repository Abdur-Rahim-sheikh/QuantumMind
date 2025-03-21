import base64

from pydantic import BaseModel

from ..repository import UrlShortenerRepository


class ShortenUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, url: str, title: str = None, description: str = None, img: base64 = None):
        return self.repository.shorten(url=url, title=title, description=description, img=img)
