from django.urls import path
from . import views
from .views import PostListView, PostDetail, CustomSignupView, ProfileView, UserCommentsView

urlpatterns = [
    # Other URL patterns...
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/comments/', views.UserCommentsView.as_view(), name='user-comments'),
]