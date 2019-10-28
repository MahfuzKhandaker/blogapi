from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Post, Comment, Reply
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, ReplySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
