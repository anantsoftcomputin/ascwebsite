# Generated by Django 3.2.5 on 2021-12-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0013_user_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_add',
            field=models.EmailField(max_length=264),
        ),
    ]