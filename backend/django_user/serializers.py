from django.contrib.auth import get_user_model
from rest_framework import serializers

DjangoUser = get_user_model()


class PasswordResetSerializer(serializers.Serializer):

    class Meta:
        model = DjangoUser
        fields = '__all__'


    # email = serializers.EmailField()
    # password = serializers.CharField(write_only=True)

