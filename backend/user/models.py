from django.db import models
from django_user.models import Django_User
from things_user_like.models import Things_User_Like
from post.models import Post
from comment.models import Comment
#from friend_request.models import Friend_Request


# Create your models here.

class User(models.Model):
    custom_django_user = models.OneToOneField(to=Django_User, on_delete=models.CASCADE, related_name='user_profile')
    job = models.CharField(max_length=30)
    # Avatar and Background image fields need to be updated.
    avatar = models.ImageField(blank=True, null=True)
    background_img = models.ImageField(blank=True, null=True)
    location = models.CharField(max_length=30)
    about_me = models.CharField(max_length=300)
    things_user_like = models.ManyToManyField(to=Things_User_Like, related_name='liked_by_user')
    posts = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='author')
    user_is_following = models.ManyToManyField('self', related_name='user_is_followed_by')
    logged_in_user_is_friend = models.ManyToManyField('self', related_name='user_is_friend')
    liked_post = models.ManyToManyField(to=Post, related_name='liked_by_user')
    comments_made = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name='author_of_comment', default=0)
    #received_request = models.ForeignKey(to=Friend_Request, on_delete=models.CASCADE, related_name='receiver')
