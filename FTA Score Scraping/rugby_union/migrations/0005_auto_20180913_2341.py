# Generated by Django 2.1 on 2018-09-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rugby_union', '0004_premier15results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premier15fixtures',
            name='round',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='premier15results',
            name='away_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='premier15results',
            name='home_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='premier15results',
            name='round',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]