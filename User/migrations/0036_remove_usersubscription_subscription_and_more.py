# Generated by Django 5.1.4 on 2025-03-14 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0035_usersubscription_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubscription',
            name='subscription',
        ),
        migrations.RemoveField(
            model_name='usersubscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.DeleteModel(
            name='UserSubscription',
        ),
    ]
