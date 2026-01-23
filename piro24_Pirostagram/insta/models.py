from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    photo = models.ImageField(upload_to='posts/%y/%m/%d/', null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='post_user'
        )
    joayo = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username}의 게시물 ({self.id})"
    
class Comment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='Comment_user'
        )
    
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='post_comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

class Story(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='story_user'
        )
    photo = models.ImageField(upload_to='posts/%y/%m/%d/', null=True, blank=True)