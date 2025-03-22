import base64

from pydantic import BaseModel

from ..repository import UrlShortenerRepository


class UpdateUrlUseCase(BaseModel):
    repository: UrlShortenerRepository

    def __call__(self, pid: int, title: str = None, description: str = None, img: base64 = None):
        return self.repository.update(pid=pid, title=title, description=description, img=img)
