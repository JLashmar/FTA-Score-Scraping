# Generated by Django 2.1 on 2018-08-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0012_auto_20180827_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='match_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
