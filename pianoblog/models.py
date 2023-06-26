from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class TextPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="text_posts"
    )
    content = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='textpost_likes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class ImagePost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_posts')
    image = CloudinaryField(
        'image',
        format='jpg',
        transformation=[
            {'dpr': "auto", 'responsive': True, 'width': "auto", 'crop': "fill", 'max_width': "1080", 'max_height': "566"}
        ]
    )
    # content = ImagePostContentFormField()  # Use the custom form field
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # featured_image = models.BooleanField(default=False)
    # image_width = models.PositiveIntegerField(null=True)
    # image_height = models.PositiveIntegerField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    textpost = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name="textpost_comments")
    imagepost = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="imagepost_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.author.username}"


# class ImagePostContentFormField(SummernoteTextFormField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.widget = SummernoteInplaceWidget(attrs=self.widget_attrs)

#         # Remove toolbar buttons that are not needed for image posts
#         toolbar = self.widget_attrs.get('summernote')['toolbar']
#         toolbar.remove(['style', ['style']])
#         toolbar.remove(['font', ['bold', 'italic', 'underline', 'clear']])
#         toolbar.remove(['para', ['ul', 'ol', 'paragraph']])
#         toolbar.remove(['insert', ['link', 'video']])
#         toolbar.remove(['view', ['fullscreen', 'codeview']])



