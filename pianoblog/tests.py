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
    # Add similar tests for other models like PostComment and Profile

