from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True
        return request.user.is_authenticated and (request.user.is_admin or request.user.is_super_admin)



class IsMajor(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_major
