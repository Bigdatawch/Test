from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 分类
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="分类名称")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"

    def __str__(self):
        return self.name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="标签名称")
    
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name

# 文章
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    excerpt = models.CharField(max_length=200, blank=True, verbose_name="文章摘要")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_published = models.BooleanField(default=True, verbose_name="是否发布")

    class Meta:
        ordering = ['-created_at']
        verbose_name="文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title

# 评论
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="文章")
    author = models.CharField(max_length=100, verbose_name="评论者")
    email = models.EmailField(verbose_name="评论者邮箱")
    content = models.TextField(verbose_name="评论内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_approved = models.BooleanField(default=True, verbose_name="是否审核通过")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name="评论"
        verbose_name_plural = "评论"
        
    def __str__(self):
        return self.content