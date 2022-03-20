from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from duck_blog.models import BlogPost
from duck_blog.serializer import BlogPostSerializer

class BlogPost(generics.ListCreateAPIView):
  permission_classes  = (IsOwnerOrReadOnly,)
  queryset            = BlogPost.objects.all()
  serializer_class    = BlogPostSerializer


