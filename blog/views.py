from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .pagination import CustomPagination
from .serializers import (
    PostListSerializer,
    PostSerializer,
    CategoryListSerializer,
    CategorySerializer,
)
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

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


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    lookup_field = "pk"


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return CategoryListSerializer
        return CategorySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "pk"

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs["pk"])
