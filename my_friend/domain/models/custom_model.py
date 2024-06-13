from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.typing import base64


class CustomModel(BaseModel):
    id: int
    user_id: int
    name: str
    model_from: str
    description: str
    gender: str
    avatar: Optional[base64]
    status: str
    language: str
    age: float
    since: datetime
    parameters: dict
    private: bool
