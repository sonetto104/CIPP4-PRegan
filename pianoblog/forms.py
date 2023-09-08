from .models import PostComment, Post, ImagePost, VideoPost, TextPost, Profile
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.utils.text import slugify


class CommentForm(forms.ModelForm):
    """
    Create field/form where user can input comment.
    """
    class Meta:
        model = PostComment
        fields = ('content',)


class CustomSignupForm(SignupForm):
    """
    Create registration form with optional email field for new users.
    """
    def clean_email(self):
        # Get the email value from the form
        email = self.cleaned_data.get('email')

        # Check if email is empty or None, and if so, return an empty string
        if not email:
            return ''

        # If the email is not empty, return it
        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.save()

        Profile.objects.create(owner=user)
        return user


class ProfileForm(forms.ModelForm):
    """
    Create form where user can update profile information. Limited to bio and
    profile photo fields.
    """
    class Meta:
        model = Profile
        fields = ['bio', 'profile_photo']


class TextPostForm(forms.ModelForm):
    """
    Create the form where user will input information for text posts.
    """
    class Meta:
        model = TextPost
        fields = ['title', 'content']


class ImagePostForm(forms.ModelForm):
    """
    Create the form where user will input data for image posts.
    """
    class Meta:
        model = ImagePost
        fields = ['title', 'image']


class VideoPostForm(forms.ModelForm):
    """
    Create the form where user will input data for video posts.
    """
    class Meta:
        model = VideoPost
        fields = ['title', 'video']
