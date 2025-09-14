from django.urls import path
from .views import (
    PostListView,
    PostRetrieveUpdateDeleteView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/", PostListView.as_view(), name="add-post"),
    path("posts/<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="post-view"),
    path("posts/<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="update-post"),
    path("posts/<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="delete-post"),
    path("categories/", CategoryListCreateView.as_view(), name="categories-list"),
    path("categories/", CategoryListCreateView.as_view(), name="add-category"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDeleteView.as_view(),
        name="category-view",
    ),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDeleteView.as_view(),
        name="update-category",
    ),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDeleteView.as_view(),
        name="delete-category",
    ),
]
