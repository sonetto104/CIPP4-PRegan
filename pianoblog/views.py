from django.shortcuts import render, get_object_or_404, reverse
from .models import TextPost, ImagePost, VideoPost, Post
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views import generic


class HomePageView(TemplateView):
    """About page view"""
    
    # COULD BE CHANGED LATER FOR MORE SPECIFIC HOME HTML

    template_name = "base.html"


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    name = 'post-list'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1) 


# class MultiplePostListView(generic.ListView):
#     template_name = 'post_list.html'  # Your template for displaying the posts

#     def get_queryset(self):
#         # Retrieve all the posts and their respective types
#         queryset = Post.objects.all().select_related('content_type')
#         return queryset