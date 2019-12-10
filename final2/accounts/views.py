from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from users.forms import CustomUserCreationForm
from .forms import PostForm
from .models import Post

# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
    

# # Authenticated views
# #####################
# @login_required
# def home(request):
#   '''List of recent posts by people I follow'''
#   try:
#     my_post = Post.objects.filter(user=request.user)
#   except IndexError:
#     my_post = None
#     context = {
#         'my_post' : my_post,
#         'post_form' : PostForm
#     }
#   return render(request, 'home', context)

# # Allows to post something and shows my most recent posts.
# @login_required
# def post(request):
#   if request.method == 'POST':
#     form = PostForm(request.POST)
#     new_post = form.save(commit=False)
#     new_post.user = request.user
#     new_post.save()
#     return home(request)
#   else:
#     form = PostForm
#   return render(request, 'post.html', {'form' : form})