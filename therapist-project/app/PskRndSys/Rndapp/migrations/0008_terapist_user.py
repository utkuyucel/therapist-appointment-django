# Generated by Django 3.2.12 on 2022-03-20 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rndapp', '0007_alter_randevular_rndtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='terapist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]