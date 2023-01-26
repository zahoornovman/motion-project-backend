from django.http import HttpResponse
from rest_framework.response import Response

from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, GenericAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters


# Create your views here.

# class ListCreateUserView(ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#


# /api/users/me/ POST
# /api/users/<int:pk>/ PATCH User
class RetrieveUpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset


# /api/users/ GET all users
class ListAllUsersView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['custom_django_user__first_name', 'custom_django_user__last_name']


class GetSpecificUserView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'custom_django_user_id'
    permission_classes = [IsAuthenticated]


class ToggleFollower(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user_to_follow = Profile.objects.filter(custom_django_user=self.request.user).first()
        print(user_to_follow)
        user = self.get_object()
        if user_to_follow == user:
            return HttpResponse(content="Error: You tried to follow yourself!")
        if user_to_follow in user.user_is_followed_by.all():
            user.user_is_followed_by.remove(user_to_follow)
        else:
            user.user_is_followed_by.add(user_to_follow)
        serializer = self.get_serializer(user)
        return Response(status=200, data=serializer.data)


class ListFollowedUsers(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=Profile.objects.filter(custom_django_user=self.request.user).first())
        return obj

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset


class ListFollowers(ListAPIView):
    queryset = Profile.objects.values_list('id', 'user_is_following')
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=Profile.objects.filter(custom_django_user=self.request.user).first())
        return obj

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset
