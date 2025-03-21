from abc import ABC, abstractmethod
from base64 import base64


class UrlShortenerRepository(ABC):
    @abstractmethod
    def save(self, url: str, title: str = None, description: str = None, img: base64 = None) -> str:
        raise NotImplementedError("Implement the save method")

    @abstractmethod
    def get(self, short_url: str) -> str:
        raise NotImplementedError("Implement the get method")

    @abstractmethod
    def get_all(self) -> list:
        raise NotImplementedError("Implement the get_all method")

    @abstractmethod
    def update(self, short_url: str, title: str = None, description: str = None, img: base64 = None) -> str:
        raise NotImplementedError("Implement the update method")

    @abstractmethod
    def delete(self, short_url: str) -> str:
        raise NotImplementedError("Implement the delete method")
