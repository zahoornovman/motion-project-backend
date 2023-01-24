from friend_request.models import FriendRequest
from rest_framework import serializers


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'
