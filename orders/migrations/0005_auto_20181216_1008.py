# Generated by Django 2.1.3 on 2018-12-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181216_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_date',
            field=models.DateTimeField(),
        ),
    ]