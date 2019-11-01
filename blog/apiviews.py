from rest_framework import generics
from rest_framework import viewsets
from .models import Category, Post, Comment, Reply
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, ReplySerializer, UserSerializer
from .permissions import IsAdminOrReadOnly, IsAuthorOfCommentOrReadOnly, IsAuthorOfReplyOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 
    permission_classes = [IsAdminOrReadOnly]

class PostsInCategoryView(generics.ListAPIView): 
    serializer_class = PostSerializer 
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self): 
        pk = self.kwargs['pk'] 
        return Post.objects.filter(category=pk) 

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    permission_classes = [IsAdminOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOfCommentOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(comment_by=self.request.user)

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOfReplyOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reply_by=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]






