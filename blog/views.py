from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Category, Ticket, Like
from .mixins import Login_required_Mixin
from django.core.paginator import Paginator
from .forms import Contactusform
from django.views.generic import ListView, DetailView, FormView
# Create your views here.

'''
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})
'''
'''
def all_post(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    object_posts = paginator.get_page(page_number)
    return render(request, 'blog/all_post.html', {'posts': object_posts})
'''

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


'''
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
'''
class All_Post(Login_required_Mixin, ListView):
    model = Post
    queryset = Post.objects.published()
    template_name = 'blog/all_post.html'
    paginate_by = 2

class Detail_Post_View(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            if self.request.user.like.filter(post_id=self.object.pk, user_id=self.request.user.id).exists():
                context['is_like'] = True
            else:
                context['is_like'] = False

class Cuntact_us_View(FormView):
    template_name = 'blog/contact.html'
    form_class = Contactusform
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Ticket.objects.create(**form_data)
        return super().form_valid(form)

def like_post(request, slug, pk):
    try:
        like = Like.objects.get(post__slug=slug, user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(post_id=pk, user_id=request.user.id)
    return redirect('blog:detail', slug)
