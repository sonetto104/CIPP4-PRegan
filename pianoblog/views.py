from django.shortcuts import render, get_object_or_404, reverse
from .models import TextPost, ImagePost, VideoPost, Post, Profile, PostComment
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, UpdateView, DeleteView, CreateView
from django.views import generic
from .forms import CommentForm
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from .forms import CustomSignupForm, ProfileForm, TextPostForm, ImagePostForm, VideoPostForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout

# class HomePageView(TemplateView):
#     """About page view"""
    
#     # COULD BE CHANGED LATER FOR MORE SPECIFIC HOME HTML

#     template_name = "base.html"


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1) 


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.post_comments.filter(approved=True,).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "liked": liked,
                "commented": False,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.post_comments.filter(approved=True,).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "commented": True,
                "comment_form": CommentForm()
            }
        )


class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        # Perform any additional actions or validations
        # before saving the form

        # Call the parent class's form_valid() method
        response = super().form_valid(form)

        # Perform any additional actions after saving the form

        # Return the response
        return redirect('home')


class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, owner=user)
        posts = Post.objects.filter(author=user).order_by('-created_on')[:5]
        comments = PostComment.objects.filter(author=user)
        
        own_profile = False
        if request.user.is_authenticated and request.user == user:
            own_profile = True
        context = {
            'profile': profile,
            'posts': posts,
            'own_profile': own_profile,
            "user": user,
            "comments": comments,
        }
        return render(request, 'profile.html', context)


class UserCommentsView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        comments = PostComment.objects.filter(author=user)
        context = {
            'user': user,
            'comments': comments
        }
        return render(request, 'user_comments.html', context)


class UserPostsView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(author=user)
        context = {
            'user': user,
            'posts': posts
        }
        return render(request, 'user_posts.html', context)


class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'
    
    def get_object(self, queryset=None):
        username = self.kwargs['username']
        return get_object_or_404(Profile, owner__username=username)

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.object.owner.username})


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = PostComment
    template_name = 'delete_comment.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, {'comment': self.object})

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
    # def get_success_url(self):
    #     return reverse('profile', kwargs={'username': self.request.user.username})



    # def get_object(self, queryset=None):
    #     comment_id = self.kwargs.get('comment_id')
    #     queryset = self.get_queryset()
    #     return get_object_or_404(queryset, id=comment_id)

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return redirect(success_url)


class DeleteProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'delete_profile.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        logout(request)  # Log out the user
        user.delete()  # Delete the user profile
        return redirect(self.success_url)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    # success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, {'post': self.object})

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return redirect(self.get_success_url())


class CreatePostView(View):
    def get(self, request):
        return render(request, 'create_post.html')


class CreateTextPostView(LoginRequiredMixin, View):
    login_url = '/account_login/'
    redirect_field_name = 'next'

    def get(self, request):
        form = TextPostForm()
        return render(request, 'create_text_post.html', {'form': form})

    def post(self, request):
        form = TextPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        return render(request, 'create_text_post.html', {'form': form})


class CreateImagePostView(LoginRequiredMixin, View):
    login_url = '/account_login/'
    redirect_field_name = 'next'

    def get(self, request):
        form = ImagePostForm()
        return render(request, 'create_image_post.html', {'form': form})

    def post(self, request):
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = form.cleaned_data['title']  # Assign slug manually
            post.save()
            return redirect('home')
        return render(request, 'create_image_post.html', {'form': form})


class CreateVideoPostView(LoginRequiredMixin, View):
    login_url = '/account_login/'
    redirect_field_name = 'next'

    def get(self, request):
        form = VideoPostForm()
        return render(request, 'create_video_post.html', {'form': form})

    def post(self, request):
        form = VideoPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = form.cleaned_data['title']  # Assign slug manually
            post.save()
            return redirect('home')
        return render(request, 'create_video_post.html', {'form': form})


