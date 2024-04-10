# Generated by Django 4.2.8 on 2023-12-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0125_afiliadocodigo_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='clientejuridico',
            constraint=models.UniqueConstraint(fields=('fk_clie_juri_afil_codigo',), name='unique_afiliado_codigo_cliente_juridico'),
        ),
        migrations.AddConstraint(
            model_name='clientenatural',
            constraint=models.UniqueConstraint(fields=('fk_clie_natu_afil_codigo',), name='unique_afiliado_codigo_cliente'),
        ),
        migrations.AddConstraint(
            model_name='proveedor',
            constraint=models.UniqueConstraint(fields=('fk_prov_afil_codigo',), name='unique_afiliado_codigo_proveedor'),
        ),
    ]
