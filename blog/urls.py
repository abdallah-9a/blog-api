from django.urls import path
from .views import (
    PostListView,
    PostRetrieveView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", PostRetrieveView.as_view(), name="post-view"),
]
