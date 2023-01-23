from django.urls import path
from comment.views import ListCreateCommentView


urlpatterns = [
    path('<int:post_id>/', ListCreateCommentView.as_view()),
]
