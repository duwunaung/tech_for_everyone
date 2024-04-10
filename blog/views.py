from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def starting_page(request):
    latest_blogs = Blog.objects.all().order_by("-date")[:3]
    return render(request, "index.html", {
        "blogs": latest_blogs
    })


def blogs_page(request):
    blogs = Blog.objects.all().order_by("-date")
    return render(request, "blogs.html", {
        "blogs": blogs
    })


def blog_page(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog.html", {
        "blog": blog
    })
