from django.urls import path
from .apiviews import CommentList, CreateReply
from rest_framework.routers import DefaultRouter
from .apiviews import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = [
    # path('posts/', PostList.as_view(), name='post_list'),
    # path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/comments/', CommentList.as_view(), name='comment_list'),
    path('posts/<int:pk>/comments/<int:comment_pk>/replies/', CreateReply.as_view(), name='create_reply'),
]

urlpatterns += router.urls