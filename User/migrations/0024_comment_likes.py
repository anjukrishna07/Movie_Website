# Generated by Django 5.1.4 on 2025-02-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_comment_created_at_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
