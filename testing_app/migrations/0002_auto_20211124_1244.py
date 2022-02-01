# Generated by Django 3.2.5 on 2021-11-24 07:14

from django.db import migrations
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]
