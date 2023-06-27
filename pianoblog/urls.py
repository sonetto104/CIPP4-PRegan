from django.urls import path
from . import views
from .views import PostListView, PostDetail

urlpatterns = [
    # Other URL patterns...
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]