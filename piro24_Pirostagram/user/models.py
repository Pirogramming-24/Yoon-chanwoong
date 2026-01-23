from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(upload_to='posts/%y/%m/%d/', null=True, blank=True)
    followGuys = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers'
    )

    def __str__(self):
        return self.username