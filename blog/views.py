from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from .models import Post


@cache_page(60 * 5)
def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})


@cache_page(60 * 10)
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})
