from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    # 创建时间字段，自动设置为记录创建时的时间
    created = models.DateTimeField(auto_now_add=True)
    # 标题字段，最大长度为100，允许为空，默认值为空字符串
    title = models.CharField(max_length=100, blank=True, default="")
    # 代码内容字段，使用TextField存储长文本
    code = models.TextField()
    # 是否显示行号，布尔类型，默认为False
    linenos = models.BooleanField(default=False)
    # 语言选择字段，从预定义的LANGUAGE_CHOICES中选择，默认为'python'，最大长度100
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # 代码高亮样式字段，从预定义的STYLE_CHOICES中选择，默认为'friendly'，最大长度100
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey("auth.User", related_name="snippets", on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        # 定义模型在查询时的默认排序方式，按创建时间升序排列
        ordering = ["created"]

    def save(self, *args, **kwargs):
        """
        使用`pygments`库对代码进行高亮处理，并将结果存储在`highlighted`字段中
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

