from django.db import models
from user_profile.models import Profile


# Create your models here.

class FriendRequest(models.Model):
    class Status(models.IntegerChoices):
        ACCEPTED = 1
        REJECTED = 2
        PENDING = 0

    status = models.IntegerField(choices=Status.choices)
    request_from = models.OneToOneField(to=Profile, on_delete=models.CASCADE, related_name='requestor')
    received_by = models.OneToOneField(to=Profile, on_delete=models.CASCADE, related_name='receiver')
    # requestor = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='sent_request')
