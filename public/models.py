from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from nanoid import generate


# Create your models here.
class Account(AbstractUser):
    coins = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    version = models.CharField(max_length=100, null=True)
    redirect_url = models.CharField(
        max_length=100, help_text="Redirect url for the app"
    )
    img_base64 = models.TextField(
        null=True, blank=True, help_text="Base64 image of the app icon"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + " " + str(self.version)


class ChatSession(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    chat_name = models.CharField(max_length=100)
    conversations = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.conversations:
            self.validate_conversations(conversations=self.conversations)
        else:
            self.conversations = []

    @staticmethod
    def validate_conversations(conversations):
        if not isinstance(conversations, list):
            raise ValidationError("Conversations must be a list")
        for conversation in conversations:
            if not isinstance(conversation, dict):
                raise ValidationError("Each conversation must be a dictionary")
            if "role" not in conversation or "message" not in conversation:
                raise ValidationError("Each conversation must have a role and message")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.chat_name) + " " + str(self.user)


class CustomModel(models.Model):
    LANGUAGES = [
        ("bn", "Bengali"),
        ("en", "English"),
        ("es", "Spanish"),
        ("fr", "French"),
        ("de", "German"),
        ("it", "Italian"),
        ("pt", "Portuguese"),
        ("ru", "Russian"),
        ("zh", "Chinese"),
        ("ja", "Japanese"),
        ("ko", "Korean"),
    ]
    user = models.ForeignKey(
        Account,
        null=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(max_length=50)
    model_from = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default="neutral")
    avatar = models.TextField(
        null=True, blank=True, help_text="Base64 image of the avatar"
    )
    status = models.CharField(max_length=20, default="active")
    language = models.CharField(max_length=50, choices=LANGUAGES, default="en")
    age = models.IntegerField(default=18)
    profession = models.CharField(max_length=50, null=True, default="student")
    parameters = models.JSONField(default=dict)
    more_info = models.TextField()
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_information(self):
        details = f"""Your name is {self.name} and you are a native {self.language} speaker.
        You are {self.gender}. You are {self.age} years old and you are a {self.profession}. Also, {self.more_info}"""
        return details

    def clean(self):
        self.validate_model_name(model_name=str(self.name), username=self.user.username)

    @staticmethod
    def validate_model_name(model_name: str, username: str) -> None:
        parts = model_name.split("/")
        if len(parts) != 2 or parts[0] != username or not parts[1]:
            raise ValidationError("Model name must be in the format of 'owner/models'")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class BotFriend(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    custom_model = models.ForeignKey(CustomModel, on_delete=models.CASCADE)
    conversations = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def generate_short_url():
    return generate(size=6)


class Url(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.DO_NOTHING,
        null=True
    )
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    img_base64 = models.TextField(null=True, blank=True)
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True, editable=False, default=generate_short_url)
    ai_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
