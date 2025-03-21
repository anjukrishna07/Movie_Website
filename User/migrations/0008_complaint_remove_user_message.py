# Generated by Django 5.1.4 on 2025-02-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_user_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=25, null=True)),
                ('phones', models.IntegerField(null=True)),
                ('emails', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='message',
        ),
    ]
