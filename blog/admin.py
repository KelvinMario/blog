from django.contrib import admin
from .models import Post,Category,Tag
from comments.models import Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','name','created_time','email','url']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
