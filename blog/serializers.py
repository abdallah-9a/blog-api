from rest_framework import serializers
from .models import Post, Category, Tag


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
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name", required=False
    )
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(), slug_field="name", required=False, many=True
    )
    image = serializers.ImageField(use_url=True, required=False)

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
        read_only_fields = ["author", "slug", "created_at", "updated_at"]


def create(self, validated_data):
    tags = validated_data.pop("tags", [])
    category = validated_data.pop("category", None)
    post = Post.objects.create(**validated_data)

    if category:
        post.category = category
    post.save()

    for tag in tags:
        post.tags.add(tag)

    return post


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "posts", "created_at", "updated_at"]
