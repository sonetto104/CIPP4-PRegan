# Generated by Django 4.2.2 on 2023-06-26 21:41

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pianoblog.post')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            bases=('pianoblog.post',),
        ),
        migrations.CreateModel(
            name='TextPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pianoblog.post')),
                ('content', models.TextField(default='')),
            ],
            bases=('pianoblog.post',),
        ),
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pianoblog.post')),
                ('video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
            ],
            bases=('pianoblog.post',),
        ),
        migrations.CreateModel(
            name='VideoPostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pianoblog.comment')),
                ('videopost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videopost_comments', to='pianoblog.videopost')),
            ],
            bases=('pianoblog.comment',),
        ),
        migrations.CreateModel(
            name='TextPostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pianoblog.comment')),
                ('textpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textpost_comments', to='pianoblog.textpost')),
            ],
            bases=('pianoblog.comment',),
        ),
        migrations.CreateModel(
            name='ImagePostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pianoblog.comment')),
                ('imagepost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagepost_comments', to='pianoblog.imagepost')),
            ],
            bases=('pianoblog.comment',),
        ),
    ]
