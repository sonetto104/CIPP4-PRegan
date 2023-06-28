from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('textpost', 'imagepost', 'videopost')})
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.author.username}"


class TextPost(Post):
    content = models.TextField(default='')


class ImagePost(Post):
    image = CloudinaryField(
        'image',
        format='jpg',
        transformation=[
            {'dpr': "auto", 'responsive': True, 'width': "auto", 'crop': "fill", 'max_width': 1080, 'max_height': 566}
        ]
    )


class VideoPost(Post):
    video = CloudinaryField(
        'video',
        resource_type="video",
        eager=[
            {'max_width': 1080, 'max_height': 566, 'crop': "fill", 'audio_codec': "wav"}
        ],
        eager_async=True
    )


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True, max_length=280)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.owner)