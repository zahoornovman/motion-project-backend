from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from django_user.serializers import PasswordResetSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

DjangoUser = get_user_model()
# Create your views here.


class PasswordResetView(GenericAPIView):
    queryset = DjangoUser.objects.all
    serializer_class = PasswordResetSerializer

    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        email = serializer.validated_data["email"]
        try:
            user = DjangoUser.objects.get(email=email)
            return Response(status=status.HTTP_200_OK)
        except DjangoUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PasswordResetValidateView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        pass

