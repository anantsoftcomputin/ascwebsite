# Generated by Django 3.2.5 on 2021-12-16 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0036_auto_20211216_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Telephone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
    ]
