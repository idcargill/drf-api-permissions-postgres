from django.urls import path, include
from .views import BlogPost
from rest_framework import generics

urlpatterns = [
  path('', BlogPost.as_view(), name='blog_view'),
  path('<int:pk>/', BlogPost.as_view(), name='blog_detail'),
]
