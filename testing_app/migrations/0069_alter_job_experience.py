# Generated by Django 4.0 on 2022-01-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0068_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Experience',
            field=models.TextField(),
        ),
    ]
