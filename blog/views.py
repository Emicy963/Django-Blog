from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import PostForm
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'blog/home.html', {'posts': posts,})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')
        
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.user != post.author:
        return redirect('home_page')
    
    if request.method == 'POST':
        post.delete()
        messages.sucess(request, 'Your post has been delete!')
        return redirect('home_page')
    
    return render(request, 'blog/delete_post.html', {'post': post})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return redirect('home_page')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save
            return redirect('post_detail', id=id)
    
    else:
        form = PostForm(instance=post)

    return (request, 'blog/edit_post.html', {'form': form, 'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


""" API View """

from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

