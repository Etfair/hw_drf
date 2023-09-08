from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True

        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.user == object.owner:
            return True

        return False
