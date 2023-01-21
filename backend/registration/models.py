from django.contrib.auth import get_user_model
from django.db import models
import random

DjangoUser = get_user_model()


# Create your models here.
def code_generator(length=5):
    numbers = '0123456789'
    return "".join(random.choice(numbers) for _ in range(length))


class Registration(models.Model):
    user = models.OneToOneField(to=DjangoUser, on_delete=models.CASCADE, related_name='registration_profile')
    code = models.IntegerField(default=code_generator)
    email = models.EmailField(unique=True, blank=False)
