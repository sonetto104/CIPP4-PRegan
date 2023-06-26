from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [
    # Other URL patterns...
    path('', views.PostListView.as_view(), name='post_list'),
]