from django.contrib import admin
from .models import news,Text

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','url', 'title', 'date','category','image_url', 'editor','content')  # 在列表中显示的字段
    list_filter = ('editor', 'date')  # 筛选选项
    search_fields = ('title', 'editor')  # 搜索选项

admin.site.register(news, NewsAdmin)  # 注册模型和 Admin 类

class TextAdmin(admin.ModelAdmin):
    list_display=('text',)
    
admin.site.register(Text,TextAdmin)
