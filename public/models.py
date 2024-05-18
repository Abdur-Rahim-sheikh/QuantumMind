from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=True)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
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
