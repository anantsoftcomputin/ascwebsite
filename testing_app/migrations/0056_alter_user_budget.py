# Generated by Django 4.0 on 2022-01-01 06:05

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0055_alter_contact_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=14, null=True),
        ),
    ]
