from django.contrib import admin
from blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']
    list_filter = ['author', 'tags', 'date']
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'text', 'post']
    list_filter = ['user_name']


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Author)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)
