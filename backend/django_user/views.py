from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from django_user.serializers import PasswordResetSerializer, DjangoUserSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

DjangoUser = get_user_model()


# Create your views here.


class PasswordResetView(GenericAPIView):
    queryset = DjangoUser.objects.all()
    serializer_class = PasswordResetSerializer

    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        try:
            user = DjangoUser.objects.get(email=email)
            # Write logic to refresh code here


            # Write logic to send email with code here

            return Response({'detail': 'Password reset email sent'})
        except DjangoUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class PasswordResetValidateView(GenericAPIView):
    queryset = DjangoUser.objects.all()
    serializer_class = DjangoUserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        queryset = self.queryset()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
