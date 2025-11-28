from rest_framework import serializers
from .models import Post, Category, Tag, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'author', 'category', 'tags', 
                 'created_at', 'comment_count']
    
    def get_comment_count(self, obj):
        return obj.comments.count()

class PostDetailSerializer(PostListSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta(PostListSerializer.Meta):
        fields = PostListSerializer.Meta.fields + ['content', 'comments']