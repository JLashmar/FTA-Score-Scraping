# Generated by Django 2.1 on 2018-08-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polo', '0006_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='something',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]