from django.shortcuts import render, get_object_or_404, reverse
from .models import TextPost
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views import generic


class HomePageView(TemplateView):
    """About page view"""
    
    # COULD BE CHANGED LATER FOR MORE SPECIFIC HOME HTML

    template_name = "base.html"
