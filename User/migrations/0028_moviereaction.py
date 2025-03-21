# Generated by Django 5.1.4 on 2025-02-26 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_movies_dislikes_movies_likes'),
        ('User', '0027_comment_likes_delete_movielike'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=10)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.movies')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]
