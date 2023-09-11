from django.test import TestCase
from .forms import CommentForm


class CommentFormTest(TestCase):

    def test_comment_form_valid_data(self):
        form = CommentForm(data={'content': 'This is a test comment.'})
        self.assertTrue(form.is_valid())

    def test_comment_form_blank_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], ['This field is required.'])
