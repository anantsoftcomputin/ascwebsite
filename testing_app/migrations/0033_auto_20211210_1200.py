# Generated by Django 3.2.5 on 2021-12-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0032_auto_20211210_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cms_options',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='frontend_options',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='html_options',
            field=models.CharField(max_length=264),
        ),
    ]
