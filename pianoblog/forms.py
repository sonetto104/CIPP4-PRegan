from .models import PostComment, Post
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
        email = self.cleaned_data.get('email')
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


class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    post_type = forms.ChoiceField(choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Video')])
    author = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'post_type', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'post-field hidden'
        self.fields['image'].widget.attrs['class'] = 'post-field hidden'
        self.fields['video'].widget.attrs['class'] = 'post-field hidden'

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')
        post_type = cleaned_data.get('post_type')

        if not content and not image and not video:
            raise forms.ValidationError('You must provide content, image, or video.')

        if post_type == 'text' and (image or video):
            raise forms.ValidationError('You cannot include an image or video in a text post.')

        if post_type == 'image' and (content or video):
            raise forms.ValidationError('You cannot include content or a video in an image post.')

        if post_type == 'video' and (content or image):
            raise forms.ValidationError('You cannot include content or an image in a video post.')

        return cleaned_data

    def save(self, commit=True):
        print("Inside save method")  # Debugging statement
        post = super().save(commit=False)
        post.status = 0

        if not post.slug:  # Check if the slug field is empty
            # Generate slug based on the post's title
            slug = slugify(self.cleaned_data['title'])
            post.slug = slug

        if commit:
            post.save()
            print("Post saved in save method:", post)  # Debugging statement

        if self.cleaned_data['post_type'] == 'text':
            post.content = self.cleaned_data['content']
            post.save()  # Save the post after assigning the content

        elif self.cleaned_data['post_type'] == 'image':
            image = self.cleaned_data['image']
            ImagePost.objects.create(post=post, image=image)

        elif self.cleaned_data['post_type'] == 'video':
            video = self.cleaned_data['video']
            VideoPost.objects.create(post=post, video=video)
    
        print("Post objects count after save:", Post.objects.count())  # Debugging statement
    
        return post