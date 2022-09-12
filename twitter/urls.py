
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
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


)
from posts.views import (
    PostListView
)
urlpatterns = [
       path('',  PostListView.as_view(), name='postlist'),
       path('landing',  LandingView.as_view(), name='landing'),
       path('admin/', admin.site.urls),
       path('posts/', include('posts.urls', namespace="posts")),
       path('user/', include('user.urls', namespace="user")),
       path('login/', LoginView.as_view(), name="login"),
       path('signup/', SignupView.as_view(), name="signup"),
       path('logout/', LogoutView.as_view(), name="logout"),
       path('passwordreset/', PasswordResetView.as_view(), name="password_reset_view"),
       path('passwordresetdone/', PasswordResetDoneView.as_view(), name="password_reset_done"),
       path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
       path('passwordresetcomplete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)