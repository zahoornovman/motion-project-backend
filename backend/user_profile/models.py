from django.db import models
from django_user.models import DjangoUser
from things_user_like.models import Things_User_Like


# from friend_request.models import Friend_Request


# Create your models here.

class Profile(models.Model):
    custom_django_user = models.OneToOneField(to=DjangoUser, on_delete=models.CASCADE,
                                              related_name='user_profile')
    job = models.CharField(blank=True, max_length=30)
    # Avatar and Background image fields need to be updated.
    avatar = models.ImageField(blank=True, null=True)
    background_img = models.ImageField(blank=True, null=True)
    location = models.CharField(blank=True, max_length=30)
    about_me = models.CharField(blank=True, max_length=300)
    things_user_like = models.ManyToManyField(blank=True, to=Things_User_Like, related_name='liked_by_user')

    user_is_following = models.ManyToManyField('self', related_name='user_is_followed_by', blank=True,
                                               symmetrical=False)
    friends = models.ManyToManyField('self', blank=True)


