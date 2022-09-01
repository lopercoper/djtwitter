from django.urls import path
from .views import(
    CreatePostView,
    PostListView
) 

app_name = "posts"

urlpatterns = [

    path('createpost/', CreatePostView.as_view(), name='createpost'),
    path('postlist/', PostListView.as_view(), name='postlist'),

]
