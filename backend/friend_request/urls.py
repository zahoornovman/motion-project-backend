from django.urls import path
from friend_request.views import SendFriendRequest, FriendRequestAcceptRejectDeleteList

urlpatterns = [
    path('request/<int:user_id>/', SendFriendRequest.as_view()),
    path('requests/<int:id>/', FriendRequestAcceptRejectDeleteList.as_view())
]