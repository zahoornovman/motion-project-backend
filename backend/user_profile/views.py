from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class ListCreateUserView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class UpdateAPIUserView(UpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     http_method_names = ['patch']

class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # def get_object(self):
    #     return self.request.user

    # def update(self):
