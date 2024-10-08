from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag


def main_view(request):
    return render(request, 'main.html')


def posts(request):
    return render(request, 'posts.html', context={'posts': Post.objects.all()})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    tags = Tag.objects.filter(post=post.id)
    return render(request, 'post_detail.html', context={'post': post,
                                                        'tags': tags})