# Generated by Django 5.1.4 on 2025-01-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
