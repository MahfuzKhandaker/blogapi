from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Post, Comment, Reply
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, ReplySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 

class PostsInCategoryView(generics.ListAPIView): 
    serializer_class = PostSerializer 
    def get_queryset(self): 
        pk = self.kwargs['pk'] 
        return Post.objects.filter(category=pk) 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_object(self):
        queryset = self.get_queryset()
        filter = {} 
        filter['pk'] = self.kwargs['pk'] 
        obj = get_object_or_404(queryset, **filter) 
        print(obj.main_image)
        obj.number_of_views +=1 
        obj.save() 
        return obj

class CommentList(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Comment.objects.filter(post_id=self.kwargs['pk'])
        return queryset
        
    serializer_class = CommentSerializer


class CreateReply(APIView):
    serializer_class = ReplySerializer

    def post(self, request, pk, comment_pk):
        reply_by = request.data.get('reply_by')
        reply_text = request.data.get('reply_text')
        data = {'comment': comment_pk, 'reply_by': reply_by, 'reply_text': reply_text }

        serializer = ReplySerializer(data=data)
        if serializer.is_valid():
            replies = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
