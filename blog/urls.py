from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import apiviews

router = DefaultRouter()
router.register('posts', apiviews.PostViewSet)
router.register('comments', apiviews.CommentViewSet)
router.register('replies', apiviews.ReplyViewSet)
router.register('users', apiviews.UserViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('categories', apiviews.CategoryListView.as_view(), name='categories-list'),
    path('category-filter/<int:pk>/', apiviews.PostsInCategoryView.as_view(), name='category-detail')
]

# urlpatterns += router.urls