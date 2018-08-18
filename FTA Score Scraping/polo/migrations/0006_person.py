# Generated by Django 2.1 on 2018-08-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0005_auto_20180817_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('birth_date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
