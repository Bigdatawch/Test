from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    用户序列化器类，用于将User模型实例转换为JSON格式
    继承自HyperlinkedModelSerializer，提供超链接相关的序列化功能
    """
    class Meta:
        model = User  # 指定要序列化的模型为User模型
        fields = ["url", "username", "email", "groups"]  # 指定需要序列化的字段，包括URL、用户名、邮箱和用户组

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Group序列化器类，用于将Group模型实例转换为JSON格式数据。
    继承自HyperlinkedModelSerializer，它使用超链接来表示模型关系。
    """
    class Meta:
        model = Group  # 指定要序列化的模型为Group
        fields = ["url", "name"]  # 指定序列化时包含的字段，包括url和name字段
