# Generated by Django 4.0 on 2022-01-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0059_user_seo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='seo_options',
            field=models.CharField(default='', max_length=1056),
        ),
    ]
