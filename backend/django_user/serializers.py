from django.contrib.auth import get_user_model
from rest_framework import serializers
from registration.serializers import RegistrationSerializer

DjangoUser = get_user_model()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    #password = serializers.CharField()

    # info = serializers.SerializerMethodField()
    #
    # def get_info(self, obj):
    #     return 'trying new'
    #
    # def validate_email(self, value):
    #     if 'email' :
    #         raise serializers.ValidationError('Email not registered')
    #     else:
    #       return value


class DjangoUserSerializer(serializers.ModelSerializer):
    registration = RegistrationSerializer(many=True, read_only=True)

    class Meta:
        model = DjangoUser
        fields = ['password', 'registration']
        read_only_fields = ['email']
