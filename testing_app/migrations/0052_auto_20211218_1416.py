# Generated by Django 3.2.5 on 2021-12-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0051_rename_notes_user_html_development_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cms_development_notes',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AddField(
            model_name='user',
            name='frontend_development_notes',
            field=models.CharField(default='', max_length=264),
        ),
    ]
