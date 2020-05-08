from django.contrib import admin
from .models import Post


# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'published_date', 'cover']


admin.site.register(Post, PostAdmin)
