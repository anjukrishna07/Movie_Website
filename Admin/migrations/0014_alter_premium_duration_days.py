# Generated by Django 5.1.4 on 2025-03-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premium',
            name='duration_days',
            field=models.IntegerField(),
        ),
    ]
