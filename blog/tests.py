from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    PostListView,
    CategoryListCreateView,
    PostRetrieveUpdateDeleteView,
    CategoryRetrieveUpdateDeleteView,
    CommentListCreateView,
    CommentRetrieveUpdateDeleteView,
)

# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_list_posts_url(self):
        url = reverse("posts")
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_post_detail_url(self):
        url = reverse("post-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, PostRetrieveUpdateDeleteView)

    def test_list_categories_url(self):
        url = reverse("categories")
        self.assertEqual(resolve(url).func.view_class, CategoryListCreateView)

    def test_category_detail_url(self):
        url = reverse("category-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, CategoryRetrieveUpdateDeleteView)

    def test_list_comments_url(self):
        url = reverse("comments", args=[1])
        self.assertEqual(resolve(url).func.view_class, CommentListCreateView)

    def test_comment_detail_url(self):
        url = reverse("comment-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, CommentRetrieveUpdateDeleteView)
