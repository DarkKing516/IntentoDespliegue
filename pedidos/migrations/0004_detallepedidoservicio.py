# Generated by Django 5.0.4 on 2024-04-18 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_pedido_detallepedidoproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedidoServicio',
            fields=[
                ('idDetalle_Pedido_Servicio', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_servicios', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('precio_inicial_servicio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal_servicios', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.servicio')),
            ],
            options={
                'db_table': 'detalle_pedido_servicios',
            },
        ),
    ]