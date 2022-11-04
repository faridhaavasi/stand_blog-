from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ManyToManyField(User)
    img = models.ImageField(upload_to='account/profile')
    mellicode = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.mellicode
