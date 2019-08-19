# Generated by Django 2.2.3 on 2019-08-09 18:16

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190809_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField()),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced'), ('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='single', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('next_of_kin', models.CharField(max_length=255)),
                ('nok_phone', phone_field.models.PhoneField(max_length=31)),
                ('family_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced'), ('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_joined', models.DateField()),
            ],
            options={
                'db_table': 'intercessor',
            },
        ),
        migrations.DeleteModel(
            name='Pra',
        ),
    ]
