# Generated by Django 3.2.5 on 2021-11-24 08:46

from django.db import migrations
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0002_auto_20211124_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=264, region=None, unique=True),
        ),
    ]
