# Generated by Django 5.0.4 on 2024-04-24 02:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_alter_reserva_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]