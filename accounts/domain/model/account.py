from typing import Optional

from pydantic import BaseModel, SecretStr, EmailStr


class Account(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr]
    password: SecretStr
    user_name: str
    is_superuser: bool = False
