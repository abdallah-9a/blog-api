from django.shortcuts import render
from .models import Post, Category
from .pagination import CustomPagination
from .serializers import (
    PostListSerializer,
    PostSerializer,
    CategoryListSerializer,
    CategorySerializer,
)
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


class PostListView(generics.ListCreateAPIView):
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        if self.request.method == "GET":
            return (
                Post.objects.filter(status="published")
                .select_related("author", "category")
                .prefetch_related("tags")
            )
        return Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostListSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # assign for the logged-in user


class PostRetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs["pk"], status="published")


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class CategoryRetrieveView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs["pk"])
