# Generated by Django 3.2.5 on 2021-12-09 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0019_auto_20211209_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cms_options',
        ),
        migrations.RemoveField(
            model_name='user',
            name='frontend_options',
        ),
        migrations.RemoveField(
            model_name='user',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='user',
            name='html_options',
        ),
        migrations.RemoveField(
            model_name='user',
            name='innerpages',
        ),
    ]
