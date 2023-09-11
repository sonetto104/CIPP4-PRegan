from django.test import TestCase
from django.contrib.auth.models import User
from .models import TextPost, ImagePost, VideoPost, PostComment, Profile


class ModelCreationTest(TestCase):
    def setUp(self):
        # Create a user for testing purposes
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_create_text_post(self):
        # Create a TextPost instance
        text_post = TextPost.objects.create(
            title='Test Text Post',
            slug='test-text-post',
            content='This is a test text post content.',
            status=0,  # Assuming 0 is the default status
            author=self.user  # Set the author
        )

        # Retrieve the created TextPost from the database
        saved_text_post = TextPost.objects.get(pk=text_post.pk)

        # Assert that the retrieved TextPost matches the created one
        self.assertEqual(saved_text_post.title, 'Test Text Post')
        self.assertEqual(saved_text_post.slug, 'test-text-post')
        self.assertEqual(saved_text_post.content, 'This is a test text post content.')
        self.assertEqual(saved_text_post.status, 0)
        self.assertEqual(saved_text_post.author, self.user)

    def test_create_image_post(self):
        image_id = 'Keyboard_cat_ouvbg1'  #Using 404 image stored in Cloudinary as test image

        # Create an ImagePost instance with the Cloudinary ID
        image_post = ImagePost.objects.create(
            title='Test Image Post',
            slug='test-image-post',
            image=image_id,  # Set the Cloudinary ID
            status=0,  # Assuming 0 is the default status
            author=self.user,  # Set the author
        )

        # Retrieve the created ImagePost from the database
        saved_image_post = ImagePost.objects.get(pk=image_post.pk)

        # Assert that the retrieved ImagePost matches the created one
        self.assertEqual(saved_image_post.title, 'Test Image Post')
        self.assertEqual(saved_image_post.slug, 'test-image-post')

        # Compare the image field with the expected public ID
        self.assertEqual(saved_image_post.image.public_id, image_id)
        self.assertEqual(saved_image_post.status, 0)
        self.assertEqual(saved_image_post.author, self.user)

    def test_create_video_post(self):
        video_public_id = 'prqqyzygdtxy0uf1tyap'

        # Create a VideoPost instance with the Cloudinary public ID
        video_post = VideoPost.objects.create(
            title='Test Video Post',
            slug='test-video-post',
            video=video_public_id,  # Set the Cloudinary public ID for the video
            status=0,  # Assuming 0 is the default status
            author=self.user,  # Set the author
        )

        # Retrieve the created VideoPost from the database
        saved_video_post = VideoPost.objects.get(pk=video_post.pk)

        # Assert that the retrieved VideoPost matches the created one
        self.assertEqual(saved_video_post.title, 'Test Video Post')
        self.assertEqual(saved_video_post.slug, 'test-video-post')

        # Compare the video field with the expected public ID
        self.assertEqual(saved_video_post.video.public_id, video_public_id)
        self.assertEqual(saved_video_post.status, 0)
        self.assertEqual(saved_video_post.author, self.user)

