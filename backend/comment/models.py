from django.db import models
from post.models import Post
from user_profile.models import Profile


# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    author_of_comment = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='comments_made')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
