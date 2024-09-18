from django.contrib import admin
from .models import Post,Comment,Image,Avatar

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author')
    search_fields = ('title', 'content')
    list_filter = ('published_date', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ('content', 'user__username')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')
    search_fields = ('post__title',)

admin.site.register(Avatar)
