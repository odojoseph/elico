# Generated by Django 2.2.3 on 2019-08-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_receipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tel', models.IntegerField(max_length=25)),
                ('position', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'serviceteam',
            },
        ),
        migrations.CreateModel(
            name='teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('midname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
                ('tel', models.IntegerField(max_length=25)),
                ('maritalstatus', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('famname', models.CharField(max_length=100)),
                ('villa', models.CharField(max_length=150)),
                ('home', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=250)),
                ('ministry', models.CharField(max_length=50)),
                ('datejoined', models.DateTimeField()),
                ('nextofkin', models.CharField(max_length=150)),
                ('nokadd', models.CharField(max_length=200)),
                ('noktel', models.IntegerField(max_length=25)),
            ],
            options={
                'db_table': 'teaching',
            },
        ),
    ]