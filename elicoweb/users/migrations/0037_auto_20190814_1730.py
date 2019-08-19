# Generated by Django 2.2.3 on 2019-08-14 16:30

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_auto_20190814_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg_account',
            name='credit',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='NGN', max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='pg_account',
            name='debit',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='NGN', max_digits=11, null=True),
        ),
    ]
