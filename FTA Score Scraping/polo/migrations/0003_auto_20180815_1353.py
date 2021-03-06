# Generated by Django 2.1 on 2018-08-15 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0002_auto_20180815_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='appearance_points',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='club',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='finalist_points',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='level',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='ranking',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='semi_points',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='tournament_type',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='winner_points',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='competition',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polo.Competition'),
        ),
        migrations.AddField(
            model_name='result',
            name='game_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(default='name', max_length=200),
        ),
        migrations.AlterField(
            model_name='result',
            name='team_a_score',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='team_b_score',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
