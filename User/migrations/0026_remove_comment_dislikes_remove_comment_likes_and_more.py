# Generated by Django 5.1.4 on 2025-02-25 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_remove_movies_liked_users_remove_movies_likes'),
        ('User', '0025_comment_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.CreateModel(
            name='MovieLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]
