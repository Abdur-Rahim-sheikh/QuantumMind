import base64

from pydantic import BaseModel


class Url(BaseModel):
    long_url: str
    short_url: str
    title: str = None
    description: str = None
    image: bytes = None
    ai_url: str = None

    @property
    def img_base64(self):
        return base64.b64encode(self.image).decode("utf-8") if self.image else None
