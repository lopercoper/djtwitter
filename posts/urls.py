from django.urls import path, re_path
from .views import(
    CreatePostView,
    PostListView,
    AddLike,
    RemoveLike,
    Comments,
    CreateComment
) 

app_name = "posts"

urlpatterns = [

    path('createpost/', CreatePostView.as_view(), name='createpost'),
    path('comments/<pk>/createcomment', CreateComment.as_view(), name='createcomment'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('public-profile/<pk>/likes/add',AddLike.as_view(), name="add-like"),
    path('public-profile/<pk>/likes/remove',RemoveLike.as_view(), name="remove-like"),
    path('comments/<pk>/', Comments.as_view(), name="comments")

]
