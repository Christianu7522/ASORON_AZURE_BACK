# Generated by Django 4.2.8 on 2023-12-27 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0126_clientejuridico_unique_afiliado_codigo_cliente_juridico_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='clientejuridico',
            name='unique_afiliado_codigo_cliente_juridico',
        ),
        migrations.RemoveConstraint(
            model_name='clientenatural',
            name='unique_afiliado_codigo_cliente',
        ),
        migrations.RemoveConstraint(
            model_name='proveedor',
            name='unique_afiliado_codigo_proveedor',
        ),
    ]
