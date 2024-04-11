from django.contrib import admin
from .models import Author, Tag, Blog, Comment
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "name", "email")

class BlogAdmin (admin.ModelAdmin):
    list_filter = ("author", "tags",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin (admin.ModelAdmin):
    list_display = ("user_name", "user_email", "post")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)