from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='account/profile')
    melicode = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.user.username
