from ast import Add
from urllib.parse import urlparse
from django.urls import path 
from user.views import UserView, PostList, EditProfileView, PublicProfileView,AddFollower,RemoveFollower
app_name = "user"

urlpatterns = [
    path('profile/', UserView.as_view(), name='profile'),
    path('postlist2/', PostList.as_view(), name='postlist2'),
    path('edit-profile/<pk>', EditProfileView.as_view(), name="edit-profile"),
    path('public-profile/<pk>', PublicProfileView.as_view(), name="public-profile"),
    path('public-profile/<pk>/followers/add',AddFollower.as_view(), name="add-follower"),
    path('public-profile/<pk>/followers/remove',RemoveFollower.as_view(), name="remove-follower"),
]
