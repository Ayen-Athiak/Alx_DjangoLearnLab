# blog/urls.py
from django.urls import path
from .views import register, user_login, user_logout, profile
from .views import PostCreateView,PostDeleteView,PostDetailView,PostUpdateView,PostListView,CommentCreateView,edit_comment,CommentDeleteView,CommentUpdateView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),

     path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('comment/<int:pk>/update/', CommentUpdateView, name='post_comments'),
    path('post/<int:pk>/comments/new/', CommentCreateView, name='add_comment'),
    path('comments/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete_comment'),
]
]
