# Generated by Django 3.2.5 on 2021-12-16 06:02

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0046_alter_user_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('1000'), default_currency='USD', max_digits=14),
        ),
    ]
