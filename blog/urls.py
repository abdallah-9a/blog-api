from django.urls import path
from .views import (
    PostListView,
    PostRetrieveUpdateDeleteView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
    CommentListCreateView,
    CommentRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostRetrieveUpdateDeleteView.as_view(), name="post-detail"),
    path("categories/", CategoryListCreateView.as_view(), name="categories"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDeleteView.as_view(),
        name="category-detail",
    ),
    path("posts/<int:pk>/comments/", CommentListCreateView.as_view(), name="comments"),
    path(
        "posts/comments/<int:pk>/",
        CommentRetrieveUpdateDeleteView.as_view(),
        name="comment-detail",
    ),
]
