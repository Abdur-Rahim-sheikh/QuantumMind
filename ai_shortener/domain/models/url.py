import base64

from pydantic import BaseModel


class Url(BaseModel):
    title: str
    description: str = None
    image: base64 = None
    long_url: str
    short_url: str
    ai_url: str = None
