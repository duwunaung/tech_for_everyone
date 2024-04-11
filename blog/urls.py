from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="home"),
    path("blogs", views.blogs_page, name="blogs"),
    path("blogs/<slug:slug>", views.blog_page, name="blog"),
    path("template", views.template_page)
]