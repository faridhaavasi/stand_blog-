from blog.models import Post

def recent_posts(request):
    recent_post = Post.objects.order_by('-created')[:3]

    return {'recent_post': recent_post}