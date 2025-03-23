import base64

from ..repository import UrlShortenerRepository


class UpdateUrlUseCase:
    def __init__(self, repository: UrlShortenerRepository):
        self.repository = repository

    def __call__(self, pid: int, title: str = None, description: str = None, img: base64 = None):
        return self.repository.update(pid=pid, title=title, description=description, img=img)
