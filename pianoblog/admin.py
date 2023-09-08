from django.contrib import admin
from .models import TextPost, ImagePost, VideoPost, PostComment, Profile, Post
from django_summernote.admin import SummernoteModelAdmin
from django import forms

# admin.register block taken from Code Institute's Codestar Walkthrough Project


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Add Post model to admin panel"""

    def approve_posts(modeladmin, request, queryset):
        queryset.update(status=1)

    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status", "created_on")
    search_fields = ['title']
    actions = ["approve_posts"]


@admin.register(TextPost)
class TextPostAdmin(SummernoteModelAdmin):
    """Add TextPost model to admin panel"""

    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(ImagePost)
class ImagePostAdmin(SummernoteModelAdmin):
    """Register ImagePost model to admin panel"""

    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']


@admin.register(VideoPost)
class VideoPostAdmin(SummernoteModelAdmin):
    """Add VideoPost model to admin panel"""
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    """Add PostComment model to admin panel"""

    list_display = ('author', 'content', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author_username', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """"Add Profile model to admin panel"""

    list_display = ('owner', 'created_on', 'status')
    list_filter = ('status', 'created_on')
    search_fields = ('owner', 'content')

    actions = ['approve_profile']

    def approve_profile(self, request, queryset):
        queryset.update(approved=True)
