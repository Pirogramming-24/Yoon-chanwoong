from django.db import models

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=100, default='empty_title')
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    content = models.TextField(default='empty_content')
    interest = models.CharField(max_length=100, default='empty_interest')
    devtool = models.CharField(max_length=100, default='empty_devtool')