from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

STATUS = ((0, "Draft"), (1, "Published"))




# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     likes = models.ManyToManyField(
#         User, related_name='blogpost_like', blank=True)

#     class Meta:
#         ordering = ["-created_on"]

#     def __str__(self):
#         return self.title

#     def number_of_likes(self):
#         return self.likes.count()


# class TextPost(Post):
#     content = models.TextField(default='')


# class ImagePost(Post):
#     image = CloudinaryField(
#         'image',
#         format='jpg',
#         transformation=[
#             {'dpr': "auto", 'responsive': True, 'width': "auto", 'crop': "fill", 'max_width': 1080, 'max_height': 566}
#         ]
#     )


# class VideoPost(Post):
#     video = CloudinaryField(
#         'video',
#         resource_type="video",
#         eager=[
#             {'max_width': 1080, 'max_height': 566, 'crop': "fill", 'audio_codec': "wav"}
#         ],
#         eager_async=True
#     )



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.author.username}"


# class TextPostComment(Comment):
#     textpost = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name="textpost_comments")


# class ImagePostComment(Comment):
#     imagepost = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="imagepost_comments")


# class VideoPostComment(Comment):
#     videopost = models.ForeignKey(VideoPost, on_delete=models.CASCADE, related_name="videopost_comments")    


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)
    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()




class TextPost(Post):
    content = models.TextField(default='')


class TextPostComment(Comment):
    textpost = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name="textpost_comments")


class ImagePost(Post):
    image = CloudinaryField(
        'image',
        format='jpg',
        transformation=[
            {'dpr': "auto", 'responsive': True, 'width': "auto", 'crop': "fill", 'max_width': 1080, 'max_height': 566}
        ]
    )

class ImagePostComment(Comment):
    imagepost = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="imagepost_comments")


class VideoPost(Post):
    video = CloudinaryField(
        'video',
        resource_type="video",
        eager=[
            {'max_width': 1080, 'max_height': 566, 'crop': "fill", 'audio_codec': "wav"}
        ],
        eager_async=True
    )

class VideoPostComment(Comment):
    videopost = models.ForeignKey(VideoPost, on_delete=models.CASCADE, related_name="videopost_comments")  

# class TextPostComment(models.Model):
#     textpost = models.ForeignKey(TextPost, on_delete=models.CASCADE, related_name="textpost_comments")
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Comment {self.content} by {self.author.username}"


# class ImagePostComment(models.Model):
#     imagepost = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="imagepost_comments")
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Comment {self.content} by {self.author.username}"


# class VideoPostComment(models.Model):
#     videopost = models.ForeignKey(VideoPost, on_delete=models.CASCADE, related_name="videopost_comments")
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Comment {self.content} by {self.author.username}"


    # def post(self, request, slug, *args, **kwargs):
    #     queryset = Post.objects.filter(status=1)
    #     post = get_object_or_404(queryset, slug=slug)
    #     comments = post.comments.filter(approved=True,).order_by('created_on')
    #     liked = False
    #     if post.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #     comment_form = CommentForm(data=request.POST)

    #     if comment_form.is_valid():
    #         comment_form.instance.email = request.user.email
    #         comment_form.instance.name = request.user.username
    #         comment = comment_form.save(commit=False)
    #         comment.post = post
    #         comment.save()
    #     else:
    #         comment_form = CommentForm()

    #     return render(
    #         request,
    #         "post_detail.html",
    #         {
    #             "post": post,
    #             "comments": comments,
    #             "liked": liked,
    #             "commented": True,
    #             "comment_form": CommentForm()
    #         }
    #     )



