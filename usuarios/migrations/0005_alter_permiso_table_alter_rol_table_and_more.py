# Generated by Django 5.0.4 on 2024-04-18 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_permiso_table_alter_rol_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='permiso',
            table='permisos',
        ),
        migrations.AlterModelTable(
            name='rol',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='rolxpermiso',
            table='rolxpermiso',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuarios',
        ),
    ]
