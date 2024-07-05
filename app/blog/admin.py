from django.contrib import admin
from blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']
    list_filter = ['author', 'tags', 'date']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Author)
admin.site.register(models.Tag)
