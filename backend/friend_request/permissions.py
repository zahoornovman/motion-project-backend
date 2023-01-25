from rest_framework import request
from rest_framework.permissions import BasePermission
from user_profile.models import Profile


class IsReceiver(BasePermission):
    def has_object_permission(self, request, view, obj):
        if Profile.objects.filter(custom_django_user=request.user).first() == obj.received_by:
            return True
        else:
            return False
