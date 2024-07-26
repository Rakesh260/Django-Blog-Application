
from django.urls import path

from .views import LoginView, RegisterView, GetUserDataView, GetPosts, Logout, PostListCreateView, \
    CommentListCreateView, CommentDetailView, PostDetailView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('get-user', GetUserDataView.as_view(), name='get-user'),
    path('home', GetPosts.as_view(), name='get-posts'),
    path('create-post-blog', PostListCreateView.as_view(), name='create-post-blog'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/comments', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
]
