# Generated by Django 4.0 on 2022-01-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0071_alter_job_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='file_upload',
            field=models.FileField(upload_to='media/'),
        ),
    ]
