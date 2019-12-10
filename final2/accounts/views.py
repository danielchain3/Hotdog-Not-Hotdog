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


import hashlib
from PIL import Image

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

# def post_view(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = PostForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             cover = form.cleaned_data['cover']
#             hash = hashlib.md5(Image.open(cover).tobytes()).hexdigest()

#             form.save()
#             return HttpResponseRedirect('home.html')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})
    
# def post_view(request, id): 
#     instance = get_object_or_404(MyModel, id=id)
#     form = MyForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('next_view')
#     return render(request, 'my_template.html', {'form': form}) 

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