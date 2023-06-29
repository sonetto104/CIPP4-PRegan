from django.urls import path
from . import views
from .views import PostListView, PostDetail, CustomSignupView, ProfileView, UserCommentsView, UserPostsView, EditProfileView, DeleteCommentView

urlpatterns = [
    # Other URL patterns...
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/comments/', views.UserCommentsView.as_view(), name='user-comments'),
    path('profile/<str:username>/posts/', views.UserPostsView.as_view(), name='user-posts'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('profile/edit/<str:username>/', views.EditProfileView.as_view(), name='edit_profile'),
    path('comment/delete/<int:comment_id>/', views.DeleteCommentView.as_view(), name='delete-comment'),

]