from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    AI_one_Chatting = models.JSONField(default=list)
    AI_two_Chatting = models.JSONField(default=list)
    AI_three_Chatting = models.JSONField(default=list)

    def __str__(self):
        return self.username