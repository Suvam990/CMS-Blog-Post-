# 6. VIEWS.PY (blog/views.py)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost
import json

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'blog/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def dashboard(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/dashboard.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            BlogPost.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            messages.success(request, 'Post created successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'blog/create_post.html')

@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            post.title = title
            post.content = content
            post.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'blog/edit_post.html', {'post': post})

@login_required
@require_POST
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('dashboard')