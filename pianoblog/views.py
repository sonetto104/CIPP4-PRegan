from django.shortcuts import render, get_object_or_404, reverse
from .models import TextPost, ImagePost, VideoPost, Post, Profile, PostComment
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, UpdateView
from django.views import generic
from .forms import CommentForm
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from .forms import CustomSignupForm, ProfileForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
        context = {
            'profile': profile,
            'posts': posts,
            'own_profile': user == request.user,
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


class UserPostsView(LoginRequiredMixin, View):
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


# class EditProfileView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'edit_profile.html'
#     success_url = '/profile/'  # Redirect to profile page after successful update

#     def get_object(self, queryset=None):
#         return self.request.user.profile

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().get(request, *args, **kwargs)



# class EditProfileView(LoginRequiredMixin, View):
#     def get(self, request, username):
#         profile = get_object_or_404(Profile, owner=request.user)
#         form = ProfileForm(instance=profile)
#         context = {
#             'form': form
#         }
#         return render(request, 'edit_profile.html', context)

#     def post(self, request):
#         profile = get_object_or_404(Profile, owner=request.user)
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile', username=request.user.username)
#         context = {
#             'form': form
#         }
#         return render(request, 'edit_profile.html', context)