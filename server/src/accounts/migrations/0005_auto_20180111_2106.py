# Generated by Django 2.0.1 on 2018-01-11 15:36

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180110_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/media/default_user_image.jpg', null=True, upload_to=accounts.models.upload_location),
        ),
    ]
