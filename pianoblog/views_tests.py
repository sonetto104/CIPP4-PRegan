from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Profile, PostComment


class PostListViewTest(TestCase):
    def test_post_list_view_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class ProfileViewTest(TestCase):
    def setUp(self):
        # Create a test user and a test profile
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(owner=self.user)

    def test_profile_view_returns_200(self):
        response = self.client.get(reverse('profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)


class UserPostsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post1 = Post.objects.create(title='Post 1', slug='post-1', author=self.user)

    def test_user_posts_view_returns_200(self):
        response = self.client.get(reverse('user-posts', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)


class EditProfileViewTest(TestCase):
    def setUp(self):
        # Create a test user and a test profile
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(owner=self.user)

    def test_edit_profile_view_returns_200(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)


class DeleteProfileViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_delete_profile_view_returns_200(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_profile'))
        self.assertEqual(response.status_code, 200)


class CreateTextPostViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_text_post_view_returns_200(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_text_post'))
        self.assertEqual(response.status_code, 200)
