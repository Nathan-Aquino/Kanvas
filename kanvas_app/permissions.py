from rest_framework.permissions import BasePermission, SAFE_METHODS
import ipdb

class OnlyInstructor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser or request.method in SAFE_METHODS)

class InstructorAndStaffs(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser or request.user.is_staff)