from rest_framework.permissions import BasePermission, SAFE_METHODS

class OnlyInstructor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser or request.method in SAFE_METHODS)

class InstructorAndStaffs(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser or request.user.is_staff)

class OnlyStudent(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            return bool(request.user.is_superuser or request.user.is_staff)
        elif request.method == 'GET':
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user.is_superuser == False and request.user.is_staff == False)