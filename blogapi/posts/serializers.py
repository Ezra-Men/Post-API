from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title', 'author', 'body', 'created_at',)
        model = Post

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = User