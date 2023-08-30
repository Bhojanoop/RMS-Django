from rest_framework.exceptions import APIException
from rest_framework import permissions
from micro_auth_service.jwt.main import JwtBuilder

class NoPermissionException(APIException):
    status_code=403
    default_detail = {'info': 'no permission'}
    default_code="Forbidden"

class VendorPermission(permissions.BasePermission):

    def has_permission(self,request,view):
        token=request.META.get('HTTP_AUTHORIZATION').split(' ', 1)[1]
        if JwtBuilder(token=token).decode()['type']=='vendor':
            return True
        else:
           raise NoPermissionException()


class AdminPermission(permissions.BasePermission):

    def has_permission(self,request,view):
        token=request.META.get('HTTP_AUTHORIZATION').split(' ', 1)[1]
        if JwtBuilder(token=token).decode()['type']=='admin':
            return True
        else:
           raise NoPermissionException()