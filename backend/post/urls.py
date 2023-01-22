from django.urls import path, include
from post.views import ListCreatePostView, RetrieveUpdateDeletePostView, SearchPostView

urlpatterns = [
    path('', ListCreatePostView.as_view()),
    path('<pk>/', RetrieveUpdateDeletePostView.as_view()),
]
