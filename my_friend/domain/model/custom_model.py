from pydantic import BaseModel


class CustomModel(BaseModel):
    id: int
    user_id: int
    model_name: str
    model_from: str
    system_instruction: str
    parameters: dict
