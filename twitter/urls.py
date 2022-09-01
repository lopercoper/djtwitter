
from django.contrib import admin
from django.urls import path,include

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from main.views import (
    LandingView,
    SignupView,
    EditProfileView,


)
from posts.views import (
    PostListView
)
urlpatterns = [
       path('',  PostListView.as_view(), name='postlist'),
       path('landing',  LandingView.as_view(), name='landing'),
       path('admin/', admin.site.urls),
       path('posts/', include('posts.urls', namespace="posts")),
       path('login/', LoginView.as_view(), name="login"),
       path('signup/', SignupView.as_view(), name="signup"),
       path('logout/', LogoutView.as_view(), name="logout"),
       path('passwordreset/', PasswordResetView.as_view(), name="password_reset_view"),
       path('passwordresetdone/', PasswordResetDoneView.as_view(), name="password_reset_done"),
       path('edit-profile/<pk>', EditProfileView.as_view(), name="edit_profile"),
       path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
       path('passwordresetcomplete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),




]
