# Generated by Django 3.2.12 on 2022-05-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rndapp', '0032_alter_randevular_rndtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randevular',
            name='rndTime',
            field=models.DateTimeField(default='17/05/2022 18:08'),
        ),
    ]
