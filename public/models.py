from django.contrib.auth.models import AbstractUser
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
    chat_id = models.IntegerField()
    chat_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chat_name) + " " + str(self.user)


class Conversation(models.Model):
    Participant = models.TextChoices("user", "bot")
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    message = models.TextField()
    role = models.CharField(max_length=20, choices=Participant)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.message) + " " + str(self.role)
