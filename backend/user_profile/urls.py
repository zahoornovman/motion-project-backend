from django.urls import path, include
from user_profile.views import ListCreateUserView

urlpatterns = [
    path('', ListCreateUserView.as_view())
]
