# Generated by Django 2.0.1 on 2018-01-10 08:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20180110_1337'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together={('from_user', 'to_user')},
        ),
    ]