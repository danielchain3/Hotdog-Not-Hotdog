from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/', views.CreatePostView.as_view(), name='add_post'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
