# Generated by Django 2.1.3 on 2018-12-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_pic', models.ImageField(blank=True, upload_to='uploaded')),
            ],
        ),
    ]
