from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    img = models.ImageField(upload_to='account/profile', verbose_name='تصویر')
    melicode = models.CharField(max_length=11, unique=True, verbose_name='کد ملی')

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'
