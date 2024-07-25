
from django.urls import path

from .views import LoginView, RegisterView, GetUserDataView, GetPosts, Logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('get-user/', GetUserDataView.as_view(), name='get-user'),
    path('home/', GetPosts.as_view(), name='get-posts'),
]
