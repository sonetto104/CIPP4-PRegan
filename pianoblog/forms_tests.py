from django.test import TestCase
from .forms import CommentForm, CustomSignupForm, ProfileForm, TextPostForm


class CommentFormTest(TestCase):

    def test_comment_form_valid_data(self):
        form = CommentForm(data={'content': 'This is a test comment.'})
        self.assertTrue(form.is_valid())

    def test_comment_form_blank_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], ['This field is required.'])


class CustomSignupFormTest(TestCase):

    def test_signup_form_valid_data(self):
        form = CustomSignupForm(data={'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_signup_form_blank_data(self):
        form = CustomSignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])


class ProfileFormTest(TestCase):

    def test_profile_form_valid_data(self):
        form = ProfileForm(data={'bio': 'This is a test bio.'})
        self.assertTrue(form.is_valid())

    def test_profile_form_blank_data(self):
        form = ProfileForm(data={})
        self.assertTrue(form.is_valid())  # The form allows blank fields


class TextPostFormTest(TestCase):

    def test_text_post_form_valid_data(self):
        form = TextPostForm(data={'title': 'Test Title', 'content': 'This is a test content.'})
        self.assertTrue(form.is_valid())

    def test_text_post_form_blank_data(self):
        form = TextPostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])