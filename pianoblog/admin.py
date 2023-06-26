from django.contrib import admin
from .models import TextPost, Comment, ImagePost
from django_summernote.admin import SummernoteModelAdmin

# admin.register block taken from Code Institute's Codestar Walkthrough Project


@admin.register(TextPost)
class TextPostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    summernote_fields = ('content')


# class ImagePostContentFormField(SummernoteTextFormField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.widget = SummernoteInplaceWidget(attrs=self.widget_attrs)

#         # Remove toolbar buttons that are not needed for image posts
#         toolbar = self.widget_attrs.get('summernote')['toolbar']
#         toolbar.remove(['style', ['style']])
#         toolbar.remove(['font', ['bold', 'italic', 'underline', 'clear']])
#         toolbar.remove(['para', ['ul', 'ol', 'paragraph']])
#         toolbar.remove(['insert', ['link', 'video']])
#         toolbar.remove(['view', ['fullscreen', 'codeview']])


@admin.register(ImagePost)
class ImagePostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']

# admin.register block taken from Code Institute's Codestar Walkthrough Project

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'textpost', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
