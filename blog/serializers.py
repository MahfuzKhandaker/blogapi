from rest_framework import serializers
from .models import Category, Post, Comment, Reply
import re
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
    main_image = serializers.SerializerMethodField('get_profile_pic_url')
    comments = CommentSerializer(many= True, required=False)
    class Meta:
        model = Post
        fields = '__all__'

    def get_profile_pic_url(self, obj):
        request = self.context.get('request')
        return (re.sub('/([-\w])+/media/media/','/media/media/', request.build_absolute_uri(obj.main_image.url), 1))




