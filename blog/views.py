from django.shortcuts import render, get_object_or_404

from .models import Category, Post
# Create your views here.

def blog(request):
    posts = Post.objects.filter(active=True)

    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, pk):
    category = get_object_or_404(Category, id=pk)
    #posts = Post.objects.filter(active=True, categories=category)
    #return render(request, 'blog/category.html', {'category': category, 'posts': posts})
    return render(request, 'blog/category.html', {'category': category})