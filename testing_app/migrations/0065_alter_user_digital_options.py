# Generated by Django 4.0 on 2022-01-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0064_alter_user_digital_options_alter_user_seo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='digital_options',
            field=models.CharField(default='', max_length=1024),
        ),
    ]