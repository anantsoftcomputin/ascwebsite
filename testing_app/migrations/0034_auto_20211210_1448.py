# Generated by Django 3.2.5 on 2021-12-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0033_auto_20211210_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='homepage',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='innerpages',
            field=models.IntegerField(default=''),
        ),
    ]