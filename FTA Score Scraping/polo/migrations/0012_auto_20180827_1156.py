# Generated by Django 2.1 on 2018-08-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0011_auto_20180818_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='game_date',
            new_name='match_date',
        ),
        migrations.AddField(
            model_name='result',
            name='stage',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
