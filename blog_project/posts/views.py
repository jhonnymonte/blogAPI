from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializers, UserSerializer


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
