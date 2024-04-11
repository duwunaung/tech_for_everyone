from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def starting_page(request):
    latest_blogs = Blog.objects.all().order_by("-id")[:3]
    return render(request, "index.html", {
        "blogs": latest_blogs,
        "current_page": "home"
    })


def blogs_page(request):
    blogs = Blog.objects.all().order_by("-date")
    return render(request, "blogs.html", {
        "blogs": blogs,
        "current_page": "blogs"
    })


def blog_page(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog.html", {
        "blog": blog,
        "tags": blog.tags.all(),
        "current_page": "blogs"
    })


def template_page(request):
    return render(request, "template.html")
