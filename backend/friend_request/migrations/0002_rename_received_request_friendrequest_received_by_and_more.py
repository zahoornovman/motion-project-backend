# Generated by Django 4.1.5 on 2023-01-25 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend_request', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='received_request',
            new_name='received_by',
        ),
        migrations.RenameField(
            model_name='friendrequest',
            old_name='sent_request',
            new_name='request_from',
        ),
    ]
