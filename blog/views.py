from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator
# Create your views here.

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

def all_post(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    object_posts = paginator.get_page(page_number)
    return render(request, 'blog/all_post.html', {'posts': object_posts})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.all()  # related name
    return render(request, 'blog/all_post.html', {'posts': posts})
def serch_post(request):
    q = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=q, body__icontains=q)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    object_posts = paginator.get_page(page_number)
    return render(request, 'blog/all_post.html', {'posts': object_posts})

