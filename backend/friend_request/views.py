from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from friend_request.models import FriendRequest
from user_profile.models import Profile
from friend_request.serializers import FriendRequestSerializer
from django.db import DatabaseError
from friend_request.permissions import IsReceiver


class SendFriendRequest(ListCreateAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(request_from=self.request.user.id)

    def create(self, request: Request, *args, **kwargs):
        requestee_id = kwargs['user_id']
        try:
            requestee = Profile.objects.get(id=requestee_id)
        except FriendRequest.DoesNotExist:
            return Response(data='The id does not exist', status=status.HTTP_404_NOT_FOUND)

        try:
            requestor = Profile.objects.filter(custom_django_user=self.request.user).first()
            if FriendRequest.objects.filter(received_by=requestee,
                                            request_from=requestor).exists() or FriendRequest.objects.filter(
                request_from=requestee, received_by=requestor).exists():
                return Response(data='Friend already exists!', status=status.HTTP_200_OK)
            else:
                friend_request = FriendRequest.objects.create(received_by=requestee, request_from=requestor,
                                                              status=0)
                friend_request.save()
                return Response(data="Friend request created!", status=status.HTTP_201_CREATED)
        except DatabaseError or ValueError:
            return Response(data='Something is not right...', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FriendRequestAcceptRejectDeleteList(RetrieveUpdateDestroyAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsReceiver]
    lookup_field = "id"
