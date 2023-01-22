# from django.urls import path
#
# from PasswordRestViews.views import
#
# urlpatterns = [
#     path('', ListCreateItemsView.as_view()),
#     path('<int:item_id>/', RetrieveUpdateDeleteItemView.as_view()),
# ]
from django.urls import path
from django_user.views import PasswordResetView, PasswordResetValidateView

urlpatterns = [
    path('', PasswordResetView.as_view()),
    path('validate/', PasswordResetValidateView.as_view())
]