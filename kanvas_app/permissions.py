from rest_framework.permissions import BasePermission, SAFE_METHODS
import ipdb

class OnlyInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser 