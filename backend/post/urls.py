from django.urls import path
from post.views import ListCreatePostView, RetrieveUpdateDeletePostView, ListUserPostView, ListFriendPostView, ListFollowingPostView, ListLikePostView, ToggleUpdateLikePostView

urlpatterns = [
    path('', ListCreatePostView.as_view()),
    path('<pk>/', RetrieveUpdateDeletePostView.as_view()),
    path('user/<user_id>/', ListUserPostView.as_view()),
    path('following/', ListFollowingPostView.as_view()),
    path('friends/', ListFriendPostView.as_view()),
    path('toggle-like/<int:post_id>/', ToggleUpdateLikePostView.as_view()),
    path('likes/', ListLikePostView.as_view()),
]
