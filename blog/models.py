from django.db import models
from django.conf import settings
from slugify import slugify
import re

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[:50]

    def save(self, *args, **kwargs):
        if not self.slug:
            regex_pattern = r"[^a-z0-9\+\#\._-]"
            self.slug = slugify(self.name, regex_pattern=regex_pattern, lowercase=True)

        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            regex_pattern = r"[^a-z0-9\+\#\._-]"
            self.slug = slugify(self.name, regex_pattern=regex_pattern, lowercase=True)

        return super().save(*args, **kwargs)


class Post(models.Model):
    STATUS_CHOICES = [("draft", "Draft"), ("published", "Published")]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        if not self.slug:
            regex_pattern = r"[^a-z0-9\+\#\._-]"
            self.slug = slugify(self.title, regex_pattern=regex_pattern, lowercase=True)

        return super().save(*args, **kwargs)


class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author}'s comment on {self.post}"
