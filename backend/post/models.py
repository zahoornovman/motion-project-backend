from django.db import models
from comment.models import Comment


# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=500)
    comments = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name='post', default=0)
    external_link = models.URLField
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    #Images field needs to be updated
    images = models.ImageField(blank=True, null=True)
    reposted_in = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reposted_post')
