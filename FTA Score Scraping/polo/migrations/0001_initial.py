# Generated by Django 2.1 on 2018-08-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_a', models.CharField(max_length=200)),
                ('team_a_score', models.CharField(max_length=200)),
                ('team_b', models.CharField(max_length=200)),
                ('team_b_score', models.CharField(max_length=200)),
            ],
        ),
    ]
