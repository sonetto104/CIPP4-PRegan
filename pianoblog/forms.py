from .models import PostComment, Post, ImagePost, VideoPost, TextPost
from django import forms
from .models import Profile
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.utils.text import slugify

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('content',)


class CustomSignupForm(SignupForm):
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
    class Meta:
        model = Profile
        fields = ['bio', 'profile_photo']


class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['title', 'content']


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'image']


class VideoPostForm(forms.ModelForm):
    class Meta:
        model = VideoPost
        fields = ['title', 'video']