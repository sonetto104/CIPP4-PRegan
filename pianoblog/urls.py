from django.urls import path
from . import views
from .views import PostListView, PostDetail, CustomSignupView, ProfileView, UserCommentsView, UserPostsView, EditProfileView, DeleteCommentView, DeleteProfileView, DeletePostView, PostLike

urlpatterns = [
    # Other URL patterns...
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('profile/delete/', views.DeleteProfileView.as_view(), name='delete_profile'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/comments/', views.UserCommentsView.as_view(), name='user-comments'),
    path('profile/<str:username>/posts/', views.UserPostsView.as_view(), name='user-posts'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('profile/edit/<str:username>/', views.EditProfileView.as_view(), name='edit_profile'),
    path('comment/delete/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('post/delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('create-text-post/', views.CreateTextPostView.as_view(), name='create_text_post'),
    path('create-image-post/', views.CreateImagePostView.as_view(), name='create_image_post'),
    path('create-video-post/', views.CreateVideoPostView.as_view(), name='create_video_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
   
]