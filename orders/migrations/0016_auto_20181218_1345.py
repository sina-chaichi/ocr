# Generated by Django 2.1.3 on 2018-12-18 13:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0015_auto_20181218_1215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Procces',
            new_name='Process',
        ),
    ]
