from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # picture = ?
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=512)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.title} ({self.created_date:%Y-%m-%d, %H:%M})'


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
