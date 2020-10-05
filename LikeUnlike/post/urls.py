from django.urls import path
from django.shortcuts import redirect
from .views import post_view, like_post, redirect_view

app_name = 'posts'

urlpatterns = [
	path('', post_view, name="post-list"),
	path('like/', like_post, name="like-post"),
]