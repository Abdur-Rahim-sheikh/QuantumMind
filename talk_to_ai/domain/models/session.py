from pydantic import BaseModel


class Session(BaseModel):
    id: int
    user_id: int
    name: str
    conversations: list[dict]  # list of [role, message]
