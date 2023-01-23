from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_user.serializers import PasswordResetSerializer, DjangoUserSerializer
from registration.models import Registration, code_generator

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
            # Refresh code logic here
            new_code = code_generator()
            print(new_code)
            registration = Registration.objects.get(email=user.email)
            registration.code = new_code
            registration.save()

            # Write logic to send email with code here
            send_mail(
                'Password Reset',
                f'Please find below your code for password reset: {new_code} ',
                'group01motion.backend@gmail.com',
                [email],
                fail_silently=False,
            )

            return Response({'detail': 'Email sent with code'}, status=status.HTTP_200_OK)
        except DjangoUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class PasswordResetValidateView(GenericAPIView):
    queryset = DjangoUser.objects.all()
    serializer_class = DjangoUserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            request_user = DjangoUser.objects.get(email=request.data['email'])
            actual_user = Registration.objects.get(code=request.data['code'])

            if request_user.email == actual_user.email:
                password = serializer.data['password']
                request_user.set_password(password)
                request_user.save()
                return Response({'detail': 'Password updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Code not correct for provided email'}, status=status.HTTP_404_NOT_FOUND)
        except DjangoUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Registration.DoesNotExist:
            return Response({'detail': 'Not a Valid Code'}, status=status.HTTP_404_NOT_FOUND)


