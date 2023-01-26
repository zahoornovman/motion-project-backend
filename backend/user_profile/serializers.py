from user_profile.models import Profile
from rest_framework import serializers
from django_user.serializers import DjangoUserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    custom_django_user = DjangoUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'job', 'location', 'about_me', 'custom_django_user',
                  'user_is_following', 'user_is_followed_by']

# class UserFollowedBySerializer(serializers.ModelSerializer):
#     custom_django_user = DjangoUserSerializer(read_only=True)
#
#     class Meta:
#         model = Profile
#         fields = ['custom_django_user', 'user_is_followed_by']
#
#
# class UserIsFollowingSerializer(serializers.ModelSerializer):
#     custom_django_user = DjangoUserSerializer(read_only=True)
#
#     class Meta:
#         model = Profile
#         fields = ['custom_django_user', 'user_is_following']
