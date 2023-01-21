from django.db import models
from user_profile.models import Profile


# Create your models here.

class Friend_Request(models.Model):
    class Status(models.IntegerChoices):
        ACCEPTED = 1
        REJECTED = 2
        PENDING = 0

    status = models.IntegerField(choices=Status.choices)
    requestor = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='sent_request')
