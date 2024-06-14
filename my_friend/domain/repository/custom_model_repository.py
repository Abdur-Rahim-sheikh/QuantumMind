from abc import ABC, abstractmethod
from ..models import CustomModel


class CustomModelRepository(ABC):

    @abstractmethod
    def create(self, user_id, model: CustomModel) -> None:
        pass

    @abstractmethod
    def get(self, user_id, model_id: int) -> CustomModel:
        pass

    @abstractmethod
    def get_all(self, user_id) -> list[CustomModel]:
        pass

    @abstractmethod
    def get_all_public(self) -> list[CustomModel]:
        pass

    @abstractmethod
    def update(self, user_id, model: CustomModel) -> None:
        pass

    @abstractmethod
    def delete(self, user_id, model_id: int) -> None:
        pass

    @abstractmethod
    def delete_all(self, user_id) -> None:
        pass

    @abstractmethod
    def exists(self, user_id, model_id: int) -> bool:
        pass
