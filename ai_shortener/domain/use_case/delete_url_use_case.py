from ..repository import UrlShortenerRepository


class DeleteUrlUseCase:
    def __init__(self, repository: UrlShortenerRepository):
        self.repository = repository

    def __call__(self, pid: int):
        return self.repository.delete(pid=pid)
