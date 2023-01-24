from user_profile.models import Profile
from rest_framework import serializers
from django_user.serializers import DjangoUserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    custom_django_user = DjangoUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'job', 'location', 'about_me', 'background_img', 'avatar', 'custom_django_user']
