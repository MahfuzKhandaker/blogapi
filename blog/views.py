from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()[:20]
    data = {"results": list(posts.values('main_image', 'title', 'author__username', 'body', 'publish_date', 'category__name'))}
    return JsonResponse(data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {"results": {
        'main_image': post.main_image,
        'title': post.title,
        'author__username': post.author__username,
        'body': post.body,
        'publish_date': post.publish_date, 
        'category__name': post.category__name
    }}
    return JsonResponse(data)

