from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=30, default='empty_title')
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    content = models.TextField(default='empty_content')
    interest = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0),MaxValueValidator(5)]
    )
    zzim = models.BooleanField(default=False)
    devtool = models.ForeignKey('Devtool',related_name='ideas',on_delete=models.SET_NULL, null=True)

class Devtool(models.Model):
    name = models.CharField(max_length=30, default="empty_name")
    kind = models.CharField(max_length=30, default="empty_kind")
    content = models.TextField(default="empty_content")
