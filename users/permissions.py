from rest_framework import permissions


class IsSelfOrAdminToUpdateOrDelete(permissions.BasePermission):
    message = "The user profile can be edited only by this user " \
              "or site administrator."

    def has_object_permission(self, request, view, user):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and (request.user == user or request.user.is_staff):
            return True
        return False


class IsAuthenticatedOrReadAndCreateOnly(permissions.BasePermission):
    message = "Unauthenticated user can only register or list other users."

    def has_permission(self, request, view):
        allowed_methods = permissions.SAFE_METHODS + ('POST',)
        if request.method in allowed_methods \
                or (request.user and request.user.is_authenticated):
            return True
        return False
