from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


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
