# Generated by Django 3.2.5 on 2021-12-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0021_auto_20211209_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='homepage',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='innerpages',
            field=models.IntegerField(default=1),
        ),
    ]
