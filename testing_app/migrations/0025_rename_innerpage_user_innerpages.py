# Generated by Django 3.2.5 on 2021-12-09 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0024_auto_20211209_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='innerpage',
            new_name='innerpages',
        ),
    ]
