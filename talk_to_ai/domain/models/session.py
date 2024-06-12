from pydantic import BaseModel


class Session(BaseModel):
    id: int
    user_id: int
    name: str
    conversations: list[str]  # list of [role, message]
