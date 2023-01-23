from django.contrib.auth import get_user_model
from rest_framework import serializers

DjangoUser = get_user_model()


class PasswordResetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

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
    class Meta:
        model = DjangoUser
        fields = ['email']

    # email = serializers.EmailField()
    # password = serializers.CharField(write_only=True)
