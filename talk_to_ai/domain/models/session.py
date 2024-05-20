from pydantic import BaseModel


class Session(BaseModel):
    chat_id: int
    user_id: int
    chat_name: str
    conversations: list[[str, str]]  # list of [role, message]
