# Generated by Django 2.1 on 2018-08-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0010_auto_20180818_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycomp',
            name='appearance_points',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
