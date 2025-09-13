from django.shortcuts import render
from .models import Post, Category
from .pagination import CustomPagination
from .serializers import (
    PostListSerializer,
    PostSerializer,
)
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.filter(status="published")


class PostRetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs["pk"], status="published")
