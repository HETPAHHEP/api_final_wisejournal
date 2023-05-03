from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

VERSION = 'v1'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')


urlpatterns = [
    path(f'{VERSION}/', include(router.urls)),
    path(f'{VERSION}/', include('djoser.urls')),
    path(f'{VERSION}/', include('djoser.urls.jwt')),
]
