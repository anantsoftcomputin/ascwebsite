# Generated by Django 3.2.5 on 2021-12-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0031_auto_20211210_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cms_options',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='frontend_options',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='html_options',
            field=models.CharField(default='', max_length=264),
        ),
    ]