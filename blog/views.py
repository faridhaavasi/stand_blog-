from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def detail(request, pk):
    
    return render(request, 'blog/detail.html', {})
