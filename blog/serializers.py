from rest_framework import serializers
from .models import Category, Post, Comment, Reply
from django.contrib.auth.models import User

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')

class ReplySerializer(serializers.HyperlinkedModelSerializer):
    reply_by = serializers.ReadOnlyField(source='reply_by.username')
    class Meta:
        model = Reply
        fields = ('id', 'url', 'reply_by', 'reply_text', 'comment')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment_by = serializers.ReadOnlyField(source='comment_by.username')
    replies = ReplySerializer(many= True, required=False)
    class Meta:
        model = Comment
        fields = ( 'id', 'url','comment_by', 'comment_text', 'post', 'replies')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many= True, required=False)
    class Meta:
        model = Post
        fields = ( 
                  'id',
                  'url',
                  'title',
                  'author',
                  'body',
                  'publish_date', 
                  'category', 
                  'main_image', 
                  'number_of_views', 
                  'number_of_likes', 
                  'comments',
                  )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    replies = serializers.PrimaryKeyRelatedField(many=True, queryset=Reply.objects.all())


    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'comments', 'replies']