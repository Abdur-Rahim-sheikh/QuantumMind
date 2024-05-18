from pydantic import BaseModel
from typing import Optional
import base64


class App(BaseModel):
    id: int
    name: str
    description: str
    version: Optional[str] = None
    url: str
    img_base64: Optional[str] = None

    @classmethod
    def validate_image(cls, img: str) -> Optional[str]:
        if img:
            try:
                base64.b64decode(img)
                return img
            except Exception:
                raise ValueError("Invalid base64 image")
        return None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_image
