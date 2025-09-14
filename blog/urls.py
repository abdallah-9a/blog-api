from django.urls import path
from .views import (
    PostListView,
    PostRetrieveUpdateView,
    CategoryListView,
    CategoryRetrieveView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/", PostListView.as_view(), name="add-post"),
    path("posts/<int:pk>/", PostRetrieveUpdateView.as_view(), name="update-post"),
    path("posts/<int:pk>/", PostRetrieveUpdateView.as_view(), name="post-view"),
    path("categories/", CategoryListView.as_view(), name="categories-list"),
    path("categories/<int:pk>/", CategoryRetrieveView.as_view(), name="category-view"),
]
