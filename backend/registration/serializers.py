from rest_framework import serializers

from registration.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

