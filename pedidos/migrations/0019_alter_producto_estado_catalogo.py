# Generated by Django 5.0.4 on 2024-05-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0018_alter_servicio_estado_catalogo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado_catalogo',
            field=models.CharField(max_length=1),
        ),
    ]