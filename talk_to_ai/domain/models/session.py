from pydantic import BaseModel


class Session(BaseModel):
    user_id: int
    chat_id: int
    chat_name: str
    conversations: list[str]
