from django.contrib import admin
from .models import TextPost
from django_summernote.admin import SummernoteModelAdmin

@admin.register(TextPost)
class TextPostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
