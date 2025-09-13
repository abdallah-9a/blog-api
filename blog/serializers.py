from rest_framework import serializers
from .models import Post, Category


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(read_only=True, many=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Post
        fields = ["id", "author", "title", "category", "tags", "image"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "slug",
            "content",
            "category",
            "tags",
            "status",
            "image",
            "created_at",
            "updated_at",
        ]
