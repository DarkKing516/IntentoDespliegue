# Generated by Django 5.0.4 on 2024-04-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_alter_reserva_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=80),
        ),
    ]
