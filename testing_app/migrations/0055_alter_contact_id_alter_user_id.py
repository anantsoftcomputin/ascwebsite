# Generated by Django 4.0 on 2021-12-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0054_auto_20211230_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
