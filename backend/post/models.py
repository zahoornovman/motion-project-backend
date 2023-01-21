from django.db import models
from user_profile.models import Profile


# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=500)
    external_link = models.URLField
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    #Images field needs to be updated
    images = models.ImageField(blank=True, null=True)
    reposted_in = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reposted_post')
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='posts')
    liked_by_user = models.ManyToManyField(to=Profile, related_name='liked_post', blank=True)
    #add the author -> Foreignkey to Profile