from django.urls import path
from . import views
from .views import PostListView, PostDetail, CustomSignupView

urlpatterns = [
    # Other URL patterns...
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='account_signup'),
]