# Generated by Django 5.0.4 on 2024-04-18 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_tipoproducto_producto'),
        ('usuarios', '0004_alter_permiso_table_alter_rol_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('id_Cliente', models.IntegerField()),
                ('fechaCreacion_pedido', models.DateTimeField(auto_now_add=True)),
                ('fecha_pedido', models.DateField()),
                ('descripcion_pedido', models.CharField(max_length=255)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('evidencia_pago', models.ImageField(upload_to='evidencia_pago/')),
                ('estado_pedido', models.CharField(max_length=1)),
                ('id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'db_table': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='DetallePedidoProducto',
            fields=[
                ('idDetalle_Pedido_Productos', models.AutoField(primary_key=True, serialize=False)),
                ('cant_productos', models.IntegerField()),
                ('nombre_productos', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio_inicial_producto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal_productos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.producto')),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
            ],
            options={
                'db_table': 'detalle_pedido_productos',
            },
        ),
    ]