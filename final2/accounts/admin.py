from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['name','image','hash', 'approval']
    list_editable = ['approval']

admin.site.register(Post, PostAdmin)
