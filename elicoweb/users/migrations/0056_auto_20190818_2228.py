# Generated by Django 2.2.3 on 2019-08-18 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0055_auto_20190818_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event_intercessory',
            options={'ordering': ['-created_on']},
        ),
    ]