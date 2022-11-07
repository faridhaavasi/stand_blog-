from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# my managers
from django.urls import reverse


class Post_Manager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def recent_post_published(self):
        return self.filter(status='p')[:3]

class Category_Managert(models.Manager):
    def activated(self):
        return self.filter(activate=True)

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    activate = models.BooleanField(default=True)
    objects = Category_Managert()

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish')
    )
    other = models.ForeignKey(User, on_delete=models.CASCADE) # many to one
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True,unique=True)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    img = models.ImageField(upload_to='images/blog/post')
    created = models.DateTimeField(auto_now=timezone)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES, null=False)
    objects = Post_Manager()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def get_abs_url(self):
        return reverse('blog:detail', args={self.slug})
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['updated',]
