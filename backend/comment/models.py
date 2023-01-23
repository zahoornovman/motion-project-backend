from django.db import models
from post.models import Post
from user_profile.models import Profile

from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment: {self.pk} ({self.author}) - {self.content} to {self.post}'
