from django.urls import path, include
from user_profile.views import RetrieveUpdateDeleteUserView, ListAllUsersView, GetSpecificUserView, ToggleFollower, \
    ListFollowedUsers, ListFollowers

urlpatterns = [
    path('', ListAllUsersView.as_view()),
    path('<int:custom_django_user_id>/', GetSpecificUserView.as_view()),
    path('me/', RetrieveUpdateDeleteUserView.as_view()),
    path('me/<int:pk>/', RetrieveUpdateDeleteUserView.as_view()),
    path('toggle-follow/<int:id>/', ToggleFollower.as_view()),
    path('following/', ListFollowedUsers.as_view()),
    path('followers/', ListFollowers.as_view()),
]
