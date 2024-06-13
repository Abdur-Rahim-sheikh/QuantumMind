from pydantic import BaseModel


class BotFriends(BaseModel):
    id: int
    user_id: int
    model_id: int
    conversations: list[dict]
