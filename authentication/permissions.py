from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS and request.user.is_authenticated


class AnonymousReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):
    """
    Checks if the user is admin
    """
    def has_permission(self, request, view):
        group_status = request.user.groups.filter(name='admin').exists()
        return group_status


class IsStudent(permissions.BasePermission):
    """
    Checks if the user is student
    """
    def has_permission(self, request, view):
        group_status = request.user.groups.filter(name='student').exists()
        return group_status


class IsAdminOrListOnly(permissions.BasePermission):
    """
    If the user is any type of admin allow all request, authenticated user should only be allowed list action only
    """
    def has_permission(self, request, view):
        group_status = request.user.groups.filter(name='admin').exists()
        if group_status:
            if view.action in ['create', 'list', 'retrieve', 'update', 'partial_update']:
                return True
            else:
                return False
        elif request.user.is_authenticated:
            if view.action == 'list':
                return True
            else:
                return False
        else:
            return False