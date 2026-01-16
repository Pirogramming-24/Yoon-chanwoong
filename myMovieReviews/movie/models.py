from django.db import models

class Reviews(models.Model):
    isTMDB = models.BooleanField(default=True)
    title = models.CharField(max_length=100, default='empty')
    year = models.IntegerField(default=0000)
    director = models.CharField(max_length=30, default='empty')
    hero = models.CharField(max_length=100, default='empty')
    genre = models.CharField(max_length=100, default='empty')
    score = models.FloatField(default=0.0)  
    running_hour = models.IntegerField(default=0000)
    running_minute = models.IntegerField(default=0000)
    running_total = models.IntegerField(default=0000)
    opinion = models.TextField(default='empty')
    image = models.ImageField(upload_to='static/images/',null=True, blank=True)
    movie_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title