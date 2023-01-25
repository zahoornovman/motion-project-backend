# Generated by Django 4.1.5 on 2023-01-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_profile_things_user_like'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_by_user',
        ),
        migrations.AddField(
            model_name='post',
            name='liked_by_user',
            field=models.ManyToManyField(blank=True, null=True, to='user_profile.profile'),
        ),
    ]