from blog.models import Post, Category

def recent_posts(request):
    recent_post = Post.objects.order_by('-created')[:3]

    return {'recent_post': recent_post}

def category_list(request):

    categorys = Category.objects.activated()

    return {'categorys': categorys}