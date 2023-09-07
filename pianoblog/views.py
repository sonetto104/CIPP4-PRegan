from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import TextPost, ImagePost, VideoPost, Post, Profile, PostComment
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views import generic
from django.views.generic import View, TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from .forms import CustomSignupForm, ProfileForm, TextPostForm, ImagePostForm, VideoPostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage


class PostListView(generic.ListView):
    """
    Define data to be passed to post_list.html template.
    Actually acting as homepage.
    """
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1) 
    paginate_by = 10  # Set the number of posts per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class PostDetail(View):
    """
    Define data needed to render detailed view of a post,
    including comments, date created, full content etc.
    """
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
    """
    Perform some very slight customisation on generic SignupView
    """
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
    """
    Define what data/objects are required to render profile html template.
    """
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, owner=user)
        posts = Post.objects.filter(author=user).order_by('-created_on')[:5]
        comments = PostComment.objects.filter(author=user)
        
        own_profile = False
        if request.user.is_authenticated and request.user == user:
            own_profile = True
        elif request.user.is_authenticated:
            own_profile = False
        context = {
            'profile': profile,
            'posts': posts,
            'own_profile': own_profile,
            "user": user,
            "comments": comments,
            
        }
        return render(request, 'profile.html', context)


class UserCommentsView(LoginRequiredMixin, View):
    """
    Define objects required to render comments associated 
    with a particular user.
    """
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        comments = PostComment.objects.filter(author=user)
        context = {
            'user': user,
            'comments': comments
        }
        return render(request, 'user_comments.html', context)


class UserPostsView(View):
    """
    Define objects required to render all posts associated 
    with a particular user.
    """
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(author=user)
        context = {
            'user': user,
            'posts': posts
        }
        return render(request, 'user_posts.html', context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    """
    Define how to call data required to render form 
    editing data within a user's previously existing profile.
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'
    
    def get_object(self, queryset=None):
        username = self.kwargs['username']
        return get_object_or_404(Profile, owner__username=username)

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        if request.user != profile.owner:
            return HttpResponseForbidden("You are not authorized to edit this profile.")
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.object.owner.username})


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    """
    Define objects required to render form/button that deletes
    selected comment belonging to a logged in user.
    """
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


class DeleteProfileView(LoginRequiredMixin, TemplateView):
    """
    A view for deleting a user profile.

    Attributes:
        template_name (str): The name of the HTML template for rendering the delete profile page.
        success_url (str): The URL to redirect to after successfully deleting the user profile.
    """
    template_name = 'delete_profile.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the delete profile view.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response for the delete profile page.
        """
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for deleting the user profile.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A redirect response to the success URL after deleting the user profile.
        """
        user = self.request.user
        logout(request)  # Log out the user
        user.delete()  # Delete the user profile
        return redirect(self.success_url)


class DeletePostView(LoginRequiredMixin, DeleteView):
    """
    A view for deleting a user's post.

    Attributes:
        model (class): The model class for the post to be deleted.
        template_name (str): The name of the HTML template for rendering the delete post page.
    """
    model = Post
    template_name = 'delete_post.html'
    # success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the delete post view.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response for the delete post page.
        """
        self.object = self.get_object()
        return render(request, self.template_name, {'post': self.object})

    def get_success_url(self):
        """
        Get the URL to redirect to after successfully deleting a post.

        Returns:
            str: The URL to the user's profile page.
        """
        return reverse('profile', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        """
        Get the queryset of posts to be considered for deletion.

        Returns:
            QuerySet: The queryset of posts filtered by the current user.
        """
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class CreatePostView(View):
    """
    A base view for creating a new post.
    This is an abstract view and should not be accessed directly.
    """

    def get(self, request):
        """
        Handle GET requests for creating a new post.
        Subclasses should implement this method.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response for creating a new post.
        """
        return render(request, 'create_post.html')


class CreateTextPostView(LoginRequiredMixin, View):
    """
    A view for creating a new text-based post.

    Attributes:
        login_url (str): The URL to redirect to if the user is not logged in.
        redirect_field_name (str): The name of the field to store the next URL for redirection.

    """
    login_url = '/account_login/'
    redirect_field_name = 'next'

    def get(self, request):
        """
        Handle GET requests for creating a new text-based post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response for creating a new text-based post.
        """
        form = TextPostForm()
        return render(request, 'create_text_post.html', {'form': form})

    def post(self, request):
        """
        Handle POST requests for creating a new text-based post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A redirect response to the home page after creating the post, or a validation error response.
        """
        form = TextPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            title = form.cleaned_data['title']
            slug = slugify(title)
            unique_slug = slug

            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1

            post.slug = unique_slug
            post.save()
            return redirect('home')

        return render(request, 'create_text_post.html', {'form': form})


class CreateImagePostView(LoginRequiredMixin, View):
    """
    A view for creating a new image-based post.

    Attributes:
        login_url (str): The URL to redirect to if the user is not logged in.
        redirect_field_name (str): The name of the field to store the next URL for redirection.

    """
    login_url = '/account_login/'
    redirect_field_name = 'next'

    def get(self, request):
        """
        Handle GET requests for creating a new image-based post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response for creating a new image-based post.
        """
        form = ImagePostForm()
        return render(request, 'create_image_post.html', {'form': form})

    def post(self, request):
        """
        Handle POST requests for creating a new image-based post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A redirect response to the home page after creating the post, or a validation error response.
        """
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            allowed_types = ['image/jpeg', 'image/jpg', 'image/png']

            if image_file.content_type not in allowed_types:
                form.add_error('image', 'Invalid image file format. Image files must be in jpg, jpeg or png format.')
                return render(request, 'create_image_post.html', {'form': form})

            post = form.save(commit=False)
            post.author = request.user

            title = form.cleaned_data['title']
            slug = slugify(title)
            unique_slug = slug

            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1

            post.slug = unique_slug
            post.save()
            return redirect('home')

        return render(request, 'create_image_post.html', {'form': form})


class CreateVideoPostView(LoginRequiredMixin, View):
    """
    A view for creating a new video-based post.

    Attributes:
        login_url (str): The URL to redirect to if the user is not logged in.
        redirect_field_name (str): The name of the field to store the next URL for redirection.

    """
    login_url = '/account_login/'
    redirect_field_name = 'next'

    def get(self, request):
        """
        Handle GET requests for creating a new video-based post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response for creating a new video-based post.
        """
        form = VideoPostForm()
        return render(request, 'create_video_post.html', {'form': form})

    def post(self, request):
        """
        Handle POST requests for creating a new video-based post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A redirect response to the home page after creating the post, or a validation error response.
        """
        form = VideoPostForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = form.cleaned_data['video']
            allowed_types = ['video/mp4', 'video/mpeg', 'video/quicktime']

            if video_file.content_type not in allowed_types:
                form.add_error('video', 'Invalid video file format. Video files must be mp4, mpeg or quicktime files.')
                return render(request, 'create_video_post.html', {'form': form})

            post = form.save(commit=False)
            post.author = request.user

            title = form.cleaned_data['title']
            slug = slugify(title)
            unique_slug = slug

            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1

            post.slug = unique_slug
            post.save()
            return redirect('home')

        return render(request, 'create_video_post.html', {'form': form})


class PostLike(View):
    """
    A view for handling post likes.

    Methods:
        post(self, request, slug):
            Handle POST requests for toggling a post's like status.

        Args:
            request (HttpRequest): The HTTP request object.
            slug (str): The slug of the post to toggle the like status for.

        Returns:
            HttpResponse: A redirect response to the post detail page.
    """
    def post(self, request, slug):
        """
        Handle POST requests for toggling a post's like status.

        Args:
            request (HttpRequest): The HTTP request object.
            slug (str): The slug of the post to toggle the like status for.

        Returns:
            HttpResponse: A redirect response to the post detail page.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
