import base64

from pydantic import BaseModel


class Url(BaseModel):
    long_url: str
    short_url: str
    title: str = None
    description: str = None
    image: base64 = None
    ai_url: str = None
