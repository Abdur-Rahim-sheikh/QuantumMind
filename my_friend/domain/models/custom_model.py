import base64
from datetime import datetime

from pydantic import BaseModel


class CustomModel(BaseModel):
    id: int
    user_id: int
    name: str
    model_from: str
    description: str
    gender: str
    avatar: bytes
    status: str
    language: str
    age: float
    since: datetime
    parameters: dict
    private: bool

    @property
    def avatar_base64(self):
        return base64.b64encode(self.avatar).decode("utf-8") if self.avatar else None
