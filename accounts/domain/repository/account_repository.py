from abc import ABC, abstractmethod
from ..model import Account
from typing import Optional


class AccountRepository(ABC):
    @abstractmethod
    def get_accounts(self) -> list[Account]:
        raise NotImplementedError("Implement get_accounts method")

    def get_account(
        self, user_name: Optional[str], email: Optional[str]
    ) -> Account | None:
        raise NotImplementedError("Implement get_account method")

    def add_account(self, account: Account) -> Account:
        raise NotImplementedError("Implement add_account method")

    def account_exist(self, user_name: str, email: str) -> bool:
        raise NotImplementedError("Implement account_exist method")

    def delete_account(self, user_name: str) -> bool:
        raise NotImplementedError("Implement delete_account method")

    def update_account(self, account: Account) -> Account:
        raise NotImplementedError("Implement update_account method")


# Path: accounts/domain/repository/__init__.py
