from django.contrib import admin
from .models import TextPost, ImagePost, VideoPost, PostComment
from django_summernote.admin import SummernoteModelAdmin
from django import forms

# admin.register block taken from Code Institute's Codestar Walkthrough Project


@admin.register(TextPost)
class TextPostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(ImagePost)
class ImagePostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']


@admin.register(VideoPost)
class VideoPostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']


# admin.register block taken from Code Institute's Codestar Walkthrough Project

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    # list_display = ('author', 'content', 'created_on', 'approved')
    # list_filter = ('approved', 'created_on')
    # search_fields = ('author__username', 'content')
    # actions = ['approve_comments']

    list_display = ('author', 'content', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author_username', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# @admin.register(ImagePostComment)
# class ImageCommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'content', 'imagepost', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('author__username', 'content')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)


# @admin.register(VideoPostComment)
# class VideoCommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'content', 'videopost', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('author__username', 'content')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)
