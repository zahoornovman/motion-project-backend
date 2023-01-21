from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer
from rest_framework.generics import ListCreateAPIView


# Create your views here.

class ListCreateUserView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
