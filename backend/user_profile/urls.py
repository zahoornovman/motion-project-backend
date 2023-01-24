from django.urls import path, include
from user_profile.views import ListCreateUserView, UpdateDeleteUserView

urlpatterns = [
    path('me/', ListCreateUserView.as_view()),
    path('me/<int:pk>/', UpdateDeleteUserView.as_view())
]
