from django.db import models

class Reviews(models.Model):
    # 'year = 2025'가 아니라 'IntegerField()'를 써야 DB에 저장 칸이 생깁니다.
    title = models.CharField(max_length=100, default='empty')
    year = models.IntegerField(default=0000)
    director = models.CharField(max_length=30, default='empty')
    hero = models.CharField(max_length=100, default='empty')
    genre = models.CharField(max_length=100, default='empty')
    score = models.FloatField(default=0.0)  
    running_time = models.CharField(max_length=100, default='empty')
    opinion = models.TextField(default='empty')

    def __str__(self):
        return self.title