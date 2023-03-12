from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
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
    title = models.CharField(max_length=100, verbose_name='عنوان')
    activate = models.BooleanField(default=True, verbose_name='آیا فعال باشد؟')
    objects = Category_Managert()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته ها'
class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish')
    )
    other = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده') # many to one
    title = models.CharField(max_length=20, verbose_name='عنوان')
    slug = models.SlugField(null=True, blank=True,unique=True)
    category = models.ManyToManyField(Category, related_name='posts', verbose_name='دسته بندی')
    body = models.TextField(verbose_name='متن')
    img = models.ImageField(upload_to='images/blog/post',blank=True, null=True, verbose_name='تصویر')
    created = models.DateTimeField(auto_now=timezone, verbose_name='ساخته شده ذز تاریخ')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='بروز رسانی')
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES, null=False, verbose_name='وضعیت')
    objects = Post_Manager()
    def show_post_category(self):
        category = self.category.all()
        list_of_category = ','.join([cat.title for cat in category])
        return list_of_category
    show_post_category.short_description = 'ذسته'
    def show_img(self):
        return format_html(f'<img src="{self.img.url}" lang="4'
                           f'0px;" height="40px;">')
    show_img.short_description = 'صویر'

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
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='پست مربوطه')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='reply')
    body = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
    def __str__(self):
        return self.body[:50]
class Ticket(models.Model):

    email = models.CharField(max_length=50, verbose_name='آدرس ایمیل')
    subject = models.CharField(max_length=20, verbose_name='موضوع')
    text = models.TextField(null=True, blank=True, verbose_name='متن')

    def __Str__(self):
        return f'ticket from {self.email}'
    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like', verbose_name='کاربر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like', verbose_name='پست مربوطه')
    created_at = models.DateTimeField(auto_now=True, verbose_name='زمان')

    def __abs__(self):
        return self.user
    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

