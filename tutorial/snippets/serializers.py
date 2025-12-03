from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
# class SnippetSerializer(serializers.Serializer):
#     """
#     片段(Snippet)序列化器类
#     用于将Snippet模型实例转换为JSON格式，并处理数据验证
#     继承自serializers.Serializer，提供了自动序列化/反序列化功能
#     """
#     id = serializers.IntegerField(read_only=True)
#     # 片段的唯一标识符
#     # 设置为只读，因为创建时会自动生成，不允许用户修改
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # 片段的标题
#     # 非必填字段，允许为空字符串，最大长度限制为100个字符
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     # 片段的代码内容
#     # 使用textarea.html作为基础模板，显示为多行文本框
#     linenos = serializers.BooleanField(required=False)
#     # 是否显示行号
#     # 非必填字段，布尔类型，默认为False
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     # 代码语言类型
#     # 从预定义的LANGUAGE_CHOICES中选择，默认值为'python'
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     # 代码样式类型
#     # 从预定义的STYLE_CHOICES中选择，默认值为'friendly'
#     def create(self, validated_data):
#         """
#         创建一个新的Snippet实例
#         :param validated_data: 经过验证的数据字典
#         :return: 新创建的Snippet实例
#         """
#         return Snippet.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         更新现有的Snippet实例
#         :param instance: 需要更新的Snippet实例
#         :param validated_data: 经过验证的数据字典
#         :return: 更新后的Snippet实例
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Snippet模型序列化器类
    继承自serializers.ModelSerializer，提供了自动序列化/反序列化功能
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User模型序列化器类
    用于将User模型实例转换为JSON格式，并处理数据验证和转换
    Attributes:
        snippets: 序列化器字段，表示用户关联的代码片段列表
    """
    # 使用主键关联方式序列化用户关联的多个代码片段
    # many=True 表示一个用户可以关联多个代码片段
    # queryset=Snippet.objects.all() 指定了关联查询的基础查询集
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        # 指定该序列化器对应的模型为User模型
        model = User
        # 指定序列化器包含的字段：id、用户名和关联的代码片段
        fields = ['url', 'id', 'username', 'snippets']