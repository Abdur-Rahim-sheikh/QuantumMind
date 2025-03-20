from abc import ABC, abstractmethod
from ..models import BotFriend


class BotFriendRepository(ABC):
    @abstractmethod
    def create(self, user_id: int, model_id: int) -> None:
        pass

    @abstractmethod
    def get(self, user_id: int, model_id: int) -> BotFriend:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[BotFriend]:
        pass

    @abstractmethod
    def update(self, bot_friend: BotFriend) -> None:
        pass

    @abstractmethod
    def delete(self, pk: int) -> None:
        pass

    @abstractmethod
    def delete_all(self, user_id: int) -> None:
        pass

    @abstractmethod
    def exists(self, pk: int) -> bool:
        pass
