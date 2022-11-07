from django.shortcuts import render
from blog.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.published()
    recent_post = Post.objects.recent_post_published()
    return render(request, 'home_app/index.html', {'posts': posts, 'recent_post': recent_post})