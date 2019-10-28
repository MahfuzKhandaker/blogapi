from rest_framework import serializers
from .models import Category, Post, Comment, Reply

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many= True, required=False)
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, required=False)
    class Meta:
        model = Post
        fields = '__all__'





