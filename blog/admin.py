from django.contrib import admin
from .models import Author, Tag, Blog
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "name", "email")

class BlogAdmin (admin.ModelAdmin):
    list_filter = ("author", "tags",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)