from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers, UserSerializers
from .permissions import IsAuthororReadOnly
from django.contrib.auth import get_user_model
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthororReadOnly,)
    serializer_class = UserSerializers