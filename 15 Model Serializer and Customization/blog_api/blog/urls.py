from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('hyper-posts/', views.PostListCreateHyperView.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
]
