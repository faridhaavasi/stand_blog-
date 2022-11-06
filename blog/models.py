from datetime import timezone
from django.contrib.auth.models import User
from django.db import models

# my managers
class Post_Manager(models.Manager):
    def published(self):
        return self.filter(status='p')

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
    category = models.ManyToManyField(Category)
    body = models.TextField()
    img = models.ImageField(upload_to='images/blog/post')
    created = models.DateTimeField(auto_now=timezone)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES, null=False)
    objects = Post_Manager()
    def __str__(self):
        return self.title
