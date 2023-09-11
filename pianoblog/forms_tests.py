from django.test import TestCase
from .forms import CommentForm, CustomSignupForm, ProfileForm, TextPostForm, ImagePostForm, VideoPostForm
from django.core.files.uploadedfile import SimpleUploadedFile


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


class ImagePostFormTest(TestCase):
    def test_image_post_form_valid_data(self):

        with open('./media/images/404image.jpg', 'rb') as f:
            image_content = f.read()

        # Create a temporary image file
        image_file = SimpleUploadedFile("test_image.jpg", image_content, content_type="image/jpeg")

        form_data = {
            'title': 'Test Image Post',
            'image': image_file,
        }

        # Pass the form data to the form
        form = ImagePostForm(data=form_data, files={'image': image_file})

        # Assert that the form is valid
        self.assertTrue(form.is_valid())

    def test_image_post_form_blank_data(self):
        # Create a dictionary with blank form data
        form_data = {
            'title': 'Blank Image Post',
            'image': None
        }
        form = ImagePostForm(data=form_data)

        # Assert that the form is not valid
        self.assertFalse(form.is_valid())
        # Assert that the 'image' field has an error message
        self.assertIn('image', form.errors)
        self.assertEqual(form.errors['image'], ['No file selected!'])


class VideoPostFormTest(TestCase):
    def test_video_post_form_valid_data(self):
        with open('./media/images/miriam clip.mp4', 'rb') as f:
            video_content = f.read()

        # Create a temporary video file
        video_file = SimpleUploadedFile("test_video.mp4", video_content, content_type="video/mp4")

        form_data = {
            'title': 'Test Video Post',
            'video': video_file,
        }

        # Pass the form data to the form
        form = VideoPostForm(data=form_data, files={'video': video_file})

        # Assert that the form is valid
        self.assertTrue(form.is_valid())

    def test_video_post_form_blank_data(self):
        # Create a dictionary with blank form data
        form_data = {
            'title': 'Blank Video Post',
            'video': None
        }
        form = VideoPostForm(data=form_data)

        # Assert that the form is not valid
        self.assertFalse(form.is_valid())
        # Assert that the 'video' field has an error message
        self.assertIn('video', form.errors)
        self.assertEqual(form.errors['video'], ['No file selected!'])