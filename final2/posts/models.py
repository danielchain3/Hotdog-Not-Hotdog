from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.forms import ModelForm, TextInput

# Create your models here.

class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title