from .models import PostComment
from django import forms
from .models import Profile
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('content',)


class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.save()

        Profile.objects.create(owner=user)
        return user
