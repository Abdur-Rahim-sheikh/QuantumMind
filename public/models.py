from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=True)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
