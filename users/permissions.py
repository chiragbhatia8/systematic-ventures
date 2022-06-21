from rest_framework import permissions
from users.models import User

class StudentReadAccessPermission(metaclass=permissions.BasePermissionMetaclass):
    message = "Student read access is not allowed to the current user."

    def has_permission(self, request, view):
        permissions = ["view_user"]
        
        permission = [i for i in permissions if i in User.objects.get(id=request.user.id).role.filter(name='AdminRole')]
        if permission:
            return True
        return False