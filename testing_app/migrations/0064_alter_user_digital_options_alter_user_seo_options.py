# Generated by Django 4.0 on 2022-01-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0063_user_ecom_development_notes_user_ecom_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='digital_options',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='seo_options',
            field=models.CharField(default='', max_length=264),
        ),
    ]
