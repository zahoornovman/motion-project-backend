from django.db import models
from django.contrib.auth import get_user_model
from user_profile.models import Profile

User = get_user_model()

def post_directory_path(instance, filename):
    return f'{instance.post.id}/{filename}'


class Post(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    external_link = models.URLField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to=post_directory_path, blank=True, null=True)
    reposted_post = models.ManyToManyField('self', related_name='reposted_in', blank=True,symmetrical=False)
    liked_by_user = models.ManyToManyField(to=Profile, blank=True)

    def __str__(self):
        return f'Post: {self.pk} ({self.author}) - {self.content}'
