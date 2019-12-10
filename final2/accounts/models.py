from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import CustomUser
from django.forms import ModelForm, TextInput

# from .storage import MyStorage

# Create your models here.

class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=36)
    title = models.TextField()
    cover = models.ImageField(unique=True, upload_to='images/')
    approval = models.BooleanField(default=True, editable=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title