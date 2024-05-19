from pydantic import BaseModel


class ChatSession(BaseModel):
    user_id: int
    chat_id: int
    chat_name: str
    conversations: list[str]
