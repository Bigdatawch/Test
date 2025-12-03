from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from quickstart.serializers import UserSerializer, GroupSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    用户视图集类，用于处理用户相关的HTTP请求
    继承自ModelViewSet，提供CRUD操作
    """
    queryset = User.objects.all()  # 指定查询集为所有用户
    serializer_class = UserSerializer  # 指定序列化器为UserSerializer
    permissions_classes = [permissions.IsAuthenticated]  # 指定权限类，要求用户必须通过身份验证

class GroupViewSet(viewsets.ModelViewSet):
    """
    用户组视图集类，用于处理用户组相关的HTTP请求
    继承自ModelViewSet，提供CRUD操作
    """
    queryset = Group.objects.all().order_by("name")  # 指定查询集为所有用户组
    serializer_class = GroupSerializer  # 指定序列化器为GroupSerializer
    permission_classes = [permissions.IsAuthenticated]