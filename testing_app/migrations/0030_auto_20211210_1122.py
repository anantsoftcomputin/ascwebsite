# Generated by Django 3.2.5 on 2021-12-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0029_alter_user_innerpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cms_options',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AddField(
            model_name='user',
            name='frontend_options',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AddField(
            model_name='user',
            name='html_options',
            field=models.CharField(default='', max_length=264),
        ),
    ]