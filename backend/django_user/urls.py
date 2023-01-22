
from django.urls import path
from django_user.views import PasswordResetView, PasswordResetValidateView

urlpatterns = [
    path('', PasswordResetView.as_view()),
    path('validate/', PasswordResetValidateView.as_view())
]

