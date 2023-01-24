from django.urls import path

from registration.views import NewRegistrationCreateView, NewRegistrationValidationView

urlpatterns = [
    path('', NewRegistrationCreateView.as_view()),
    path('validation/', NewRegistrationValidationView.as_view())
    ]

