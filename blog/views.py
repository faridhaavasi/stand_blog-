from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Ticket
from django.core.paginator import Paginator
from .forms import Contactusform
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

def contact(request):

    if request.method == 'POST':
        form = Contactusform(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            text = form.cleaned_data.get('text')
            if email and subject and text is not None:
                Ticket.objects.create(email=email, subject=subject, text=text)
                return redirect('home_app:home')
    else:
        form = Contactusform()
    return render(request, 'blog/contact.html', {'form': form})