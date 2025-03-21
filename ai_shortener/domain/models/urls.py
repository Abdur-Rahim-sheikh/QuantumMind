from pydantic import BaseModel
from django.contrib.auth.models import User
import base64
class Urls(BaseModel):
    title: str
    description: str = None
    image: base64 = None
    long_url: str
    short_url: str
    ai_url: str = None
