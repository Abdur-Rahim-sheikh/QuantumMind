from .repository import Repository
from ..domain.use_case import ShortenUrlUseCase, GetAllUrlsUseCase, GetUrlUseCase, UpdateUrlUseCase, DeleteUrlUseCase


class UseCase:
    def __init__(self):
        self.__repository = Repository()

    @property
    def shorten_url(self) -> ShortenUrlUseCase:
        return ShortenUrlUseCase(repository=self.__repository.url_repository)

    @property
    def get_all_urls(self) -> GetAllUrlsUseCase:
        return GetAllUrlsUseCase(repository=self.__repository.url_repository)

    @property
    def get_url(self) -> GetUrlUseCase:
        return GetUrlUseCase(repository=self.__repository.url_repository)

    @property
    def update_url(self) -> UpdateUrlUseCase:
        return UpdateUrlUseCase(repository=self.__repository.url_repository)

    @property
    def delete_url(self) -> DeleteUrlUseCase:
        return DeleteUrlUseCase(repository=self.__repository.url_repository)
