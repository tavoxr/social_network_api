from rest_framework import serializers
from drf_extra_fields import fields
from . import models


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Post
        fields = ('id', 'text', 'create_date', 'user',  'likes_count', 'comments_count') 

    def create(self, validated_data):
        post = models.Post.objects.create(**validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Comment
        fields = ('id', 'comment', 'create_date', 'user', 'post')
        read_only_fields = ('create_date',)
        extra_kwargs = {'post': {'write_only': True}}


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Like
        fields = ('id', 'user', 'post')
