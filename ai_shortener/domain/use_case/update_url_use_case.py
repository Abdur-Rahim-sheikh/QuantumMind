import base64

from pydantic import BaseModel

from ..repository import UrlShortenerRepository


class UpdateUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, short_url: str, title: str = None, description: str = None, img: base64 = None):
        return self.repository.update(short_url=short_url, title=title, description=description, img=img)
