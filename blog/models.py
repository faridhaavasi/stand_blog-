from datetime import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish')
    )
    other = models.ForeignKey(User, on_delete=models.CASCADE) # many to one
    title = models.CharField(max_length=20)
    body = models.TextField()
    img = models.ImageField(upload_to='images/blog/post')
    created = models.DateTimeField(auto_now=timezone)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES, null=False)

    def __str__(self):
        return f'{self.body[30]}'
