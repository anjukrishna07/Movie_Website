# Generated by Django 5.1.4 on 2025-02-28 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_alter_movies_dislikes_alter_movies_likes'),
        ('User', '0029_alter_moviereaction_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereaction',
            name='reaction',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='WatchLater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.movies')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]
