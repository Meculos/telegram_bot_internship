from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TelegramUsername(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    telegram_username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.telegram_username} has the id {self.telegram_id}"
