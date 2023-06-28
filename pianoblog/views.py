from django.shortcuts import render, get_object_or_404, reverse
from .models import TextPost, ImagePost, VideoPost, Post, Profile, PostComment
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views import generic
from .forms import CommentForm
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.shortcuts import redirect

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