# Generated by Django 3.2.5 on 2021-11-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0005_auto_20211126_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
