# Generated by Django 4.0 on 2022-01-04 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0058_alter_user_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seo_options',
            field=models.CharField(default='', max_length=264),
        ),
    ]