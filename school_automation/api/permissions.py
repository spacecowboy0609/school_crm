from rest_framework import permissions
from .models import *
from django.shortcuts import get_object_or_404

class IfUserExists(permissions.BasePermission):
    def has_permission(self, request, view):
        phone_number=request.data.get("phone_number")
        if UserModel.objects.filter(phone_number=phone_number).exists():
            return False 
        return True
    
class IsManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status=="manager_user":
            return True
        return False
    
class IsAdminstratorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status=="administrator_user":
            return True
        return False
    
class IsTeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status=="teacher_user":
            return True
        return False

    
class CanOverpowerObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status=="manager_user":
            return True
        elif request.user.status=="administrator_user" and obj.status in ["teacher_user","student_user"]:
            return True
        elif obj==request.user:
            return True
        return False
    
class CanUpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user==obj:
            return True
        return False
class CanDeleteUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)