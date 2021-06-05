from django.urls import path
from .views import SignUpView, UserDetailView, PostListView, PostCreateView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('createPost/', PostCreateView.as_view(), name = 'post_create'),
    path('', PostListView.as_view(), name = 'home'),
    #path('createPost/<int:pk>/', PostCreateView.as_view(), name = 'post_create'),
]