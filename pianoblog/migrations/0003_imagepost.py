# Generated by Django 4.2.2 on 2023-06-25 12:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pianoblog.image_validator


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pianoblog', '0002_textpost_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png']), pianoblog.image_validator.validate_image_size])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('featured_image', models.BooleanField(default=False)),
                ('image_width', models.PositiveIntegerField(null=True)),
                ('image_height', models.PositiveIntegerField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
