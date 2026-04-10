from rest_framework import generics
from .models import Post, Comment
from .serializers import PostHyperSerializer, PostSerializer, CommentSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListCreateHyperView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostHyperSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer