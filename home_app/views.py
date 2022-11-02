from django.shortcuts import render
from blog.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home_app/index.html', {'posts': posts})