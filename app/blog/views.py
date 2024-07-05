from django.shortcuts import render, get_object_or_404
from blog import models


def starting_page(request):
    all_posts = models.Post.objects.order_by("-date")[:3]
    print(all_posts)
    return render(request, "blog/index.html", {
        "posts": all_posts
    })


def posts(request):
    all_posts = models.Post.objects.order_by("-date").all()
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(models.Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
