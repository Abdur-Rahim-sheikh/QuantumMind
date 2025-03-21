import base64
from abc import ABC, abstractmethod
from ..models import Url

class UrlShortenerRepository(ABC):
    @abstractmethod
    def shorten(self, url: str, title: str = None, description: str = None, img: base64 = None) -> str:
        raise NotImplementedError("Implement the save method")

    @abstractmethod
    def get(self, long_url: str) -> Url:
        raise NotImplementedError("Implement the get method")

    @abstractmethod
    def get_all(self) -> list[Url]:
        raise NotImplementedError("Implement the get_all method")

    @abstractmethod
    def update(self, short_url: str, title: str = None, description: str = None, img: base64 = None) -> None:
        raise NotImplementedError("Implement the update method")

    @abstractmethod
    def delete(self, short_url: str) -> bool:
        raise NotImplementedError("Implement the delete method")
