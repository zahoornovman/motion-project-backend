# Generated by Django 4.1.5 on 2023-01-26 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=user_profile.models.user_directory_path)),
                ('background_img', models.ImageField(blank=True, null=True, upload_to=user_profile.models.user_directory_path)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('about_me', models.CharField(blank=True, max_length=300)),
                ('custom_django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(blank=True, to='user_profile.profile')),
                ('user_is_following', models.ManyToManyField(blank=True, related_name='user_is_followed_by', to='user_profile.profile')),
            ],
        ),
    ]
