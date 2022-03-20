from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from duck_blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    fields    = ('title', 'blog', 'create_date', 'updated_date')
    model     = BlogPost