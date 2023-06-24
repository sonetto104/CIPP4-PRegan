from django.contrib import admin
from .models import TextPost
from django_summernote.admin import SummernoteModelAdmin

@admin.register(TextPost)
class TextPostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    summernote_fields = ('content')
