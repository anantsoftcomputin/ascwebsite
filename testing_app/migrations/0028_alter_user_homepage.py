# Generated by Django 3.2.5 on 2021-12-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0027_auto_20211210_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='homepage',
            field=models.IntegerField(default=1),
        ),
    ]
