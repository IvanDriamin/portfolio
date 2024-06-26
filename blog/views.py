from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs':blogs})

def post(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/post.html', {'blog':blog})