# Generated by Django 3.2.12 on 2022-03-20 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rndapp', '0005_remove_randevular_rndtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='randevular',
            name='rndTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
