from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Post(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    external_link = models.URLField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # Images field needs to be updated
    images = models.ImageField(blank=True, null=True)
    reposted_post = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reposted_in', blank=True,
                                      null=True)

    def __str__(self):
        return f'Post: {self.pk} ({self.author}) - {self.content}'
