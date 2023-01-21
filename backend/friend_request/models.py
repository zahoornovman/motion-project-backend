from django.db import models
from user.models import User


# Create your models here.

class FriendRequest(models.Model):
    class Status(models.IntegerChoices):
        ACCEPTED = 1
        REJECTED = 2
        PENDING = 0

    status = models.IntegerField(choices=Status.choices)
    sent_request = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='requestor')
    received_request = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='receiver')
