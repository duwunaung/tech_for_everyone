from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        "current_page": "blogs",
        "comments": blog.comments.all().order_by("-id"),
        "comment_form": CommentForm()
    })


def save_comment(request):
    slug = request.POST["slug"]
    post = Blog.objects.get(slug=slug)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
    # print(comment_form)
    return HttpResponseRedirect(reverse("blog", args=[slug]))


def template_page(request):
    return render(request, "template.html")
