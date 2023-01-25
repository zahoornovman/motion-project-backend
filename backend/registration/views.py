from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django_user.models import DjangoUser
from registration.models import code_generator, Registration
from registration.serializers import RegistrationSerializer
from user_profile.models import Profile

DjangoUser = get_user_model()


# Create your views here.


class NewRegistrationCreateView(GenericAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']

        # Generate a validation code
        validation_code = code_generator()
        # create registration object and save
        new_registration = Registration.objects.create(email=email, code=validation_code)
        new_registration.save()
        # send mail with validation code to email address
        send_mail(
            'Email validation code',
            f'Your validation code is {validation_code}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response({"detail": "Validation code sent to email"})


class NewRegistrationValidationView(GenericAPIView):

    permission_classes = []

    def post(self, request):
        # collecting data from request
        validation_code = int(request.data['code'])
        email = request.data['email']  # serializer.data['email']
        # finding related object in Registration
        new_registration_user = Registration.objects.get(email=email)

        # comparing validation code to stored code
        if validation_code == new_registration_user.code:
            password = request.data.get('password')
            username = request.data.get('username')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            # creating and saving new custom user
            new_django_user = DjangoUser.objects.create_user(username=username, email=email,
                                                             first_name=first_name, last_name=last_name)
            new_django_user.set_password(password)
            new_django_user.save()
            # updating registration object with custom user
            Registration.objects.filter(pk=new_registration_user.id).update(user=new_django_user)
            # creating and saving new profile
            new_user_profile = Profile.objects.create(custom_django_user=new_django_user)
            new_user_profile.save()
            return Response({'detail': 'New User created. Please login'})
        else:
            return Response({'error': 'Invalid validation code'}, status=status.HTTP_400_BAD_REQUEST)

#
# class NewRegistrationCreateView(APIView):
#
#     permission_classes = []
#
#     def post(self, request):
#         email = request.data.get('email')
#         # check that the email address is not in use
#         if DjangoUser.objects.filter(email=email).exists():
#             return Response({"error": "Email address already in use"}, status=status.HTTP_400_BAD_REQUEST)
#         # Generate a validation code
#         validation_code = code_generator()
#         request.session['validation_code'] = validation_code
#         request.session['email'] = email
#         # send mail with validation code to email address
#         send_mail(
#             'Email validation code',
#             f'Your validation code is {validation_code}',
#             'from@example.com',
#             [email],
#             fail_silently=False,
#         )
#         return Response({"detail": "Validation code sent to email"})
#
#
# class NewRegistrationValidationView(APIView):
#     def post(self, request):
#         validation_code = request.data.get('validation_code')
#         if validation_code == request.session.get('validation_code'):
#             email = request.data.get('email')
#             password = request.data.get('password')
#             username = request.data.get('username')
#             user = DjangoUser.objects.create_user(username=username, email=email, password=password)
#             user_registration = Registration.objects.create(email=email, user=user, code=validation_code)
#             user.save()
#             user_registration.save()
#             return Response({"detail": "User created"})
#         else:
#             return Response({"error": "Invalid validation code"}, status=status.HTTP_400_BAD_REQUEST)
#
