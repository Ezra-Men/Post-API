from rest_framework import permissions

class IsAuthororReadOnly(permissions.BasePermission):
    #read only permissions are allowed for any request.
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
           return True
       
       #write permissions are only allowed for the author of the post
       return obj.author  == request.user
