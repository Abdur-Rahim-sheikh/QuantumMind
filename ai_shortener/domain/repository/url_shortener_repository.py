import base64
from abc import ABC, abstractmethod
from typing import Optional

from ..models import Url


class UrlShortenerRepository(ABC):
    @abstractmethod
    def shorten(self, long_url: str, title: str = None, description: str = None, img: base64 = None) -> Url:
        raise NotImplementedError("Implement the save method")

    @abstractmethod
    def get(self, pid: int) -> Optional[Url]:
        raise NotImplementedError("Implement the get method")

    @abstractmethod
    def get_all(self) -> list[Url]:
        raise NotImplementedError("Implement the get_all method")

    @abstractmethod
    def update(self, pid: int, title: str = None, description: str = None, img: base64 = None) -> None:
        raise NotImplementedError("Implement the update method")

    @abstractmethod
    def delete(self, pid: int) -> bool:
        raise NotImplementedError("Implement the delete method")
