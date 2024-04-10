# Generated by Django 4.2.8 on 2023-12-26 22:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0118_historicodolar_venta_ventastatus_fk_venta_stat_vent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('cheq_id', models.AutoField(primary_key=True, serialize=False, verbose_name='identificador')),
                ('cheq_numero_cheque', models.CharField(max_length=50, verbose_name='Numero de cheque')),
                ('cheq_banco', models.CharField(max_length=50, verbose_name='Banco')),
                ('fk_cheq_clie_juri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientejuridico', verbose_name='Cliente Juridico')),
                ('fk_cheq_clie_natu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientenatural', verbose_name='Cliente Natural')),
            ],
            options={
                'verbose_name_plural': 'Cheque',
            },
        ),
        migrations.CreateModel(
            name='Efectivo',
            fields=[
                ('efe_id', models.AutoField(primary_key=True, serialize=False, verbose_name='identificador')),
                ('efe_monto', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Monto')),
                ('fk_efe_clie_juri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientejuridico', verbose_name='Cliente Juridico')),
                ('fk_efe_clie_natu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientenatural', verbose_name='Cliente Natural')),
            ],
            options={
                'verbose_name_plural': 'Efectivo',
            },
        ),
        migrations.CreateModel(
            name='TarjetaCredito',
            fields=[
                ('tdc_id', models.AutoField(primary_key=True, serialize=False, verbose_name='identificador')),
                ('tdc_numero_tarjeta', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='Numero de tarjeta')),
                ('tdc_nombre_titular', models.CharField(max_length=50, verbose_name='Nombre del titular')),
                ('tdc_fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('tdc_cvv', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='CVV')),
                ('fk_tdc_clie_juri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientejuridico', verbose_name='Cliente Juridico')),
                ('fk_tdc_clie_natu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientenatural', verbose_name='Cliente Natural')),
            ],
            options={
                'verbose_name_plural': 'Tarjeta de Credito',
            },
        ),
        migrations.CreateModel(
            name='Puntos',
            fields=[
                ('punt_id', models.AutoField(primary_key=True, serialize=False, verbose_name='identificador')),
                ('punt_cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('fk_punt_clie_juri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientejuridico', verbose_name='Cliente Juridico')),
                ('fk_punt_clie_natu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.clientenatural', verbose_name='Cliente Natural')),
            ],
            options={
                'verbose_name_plural': 'Puntos',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('pago_id', models.AutoField(primary_key=True, serialize=False, verbose_name='identificador')),
                ('pago_cantidad_pagada', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Cantidad pagada')),
                ('fk_pago_cheq', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.cheque', verbose_name='Cheque')),
                ('fk_pago_efe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.efectivo', verbose_name='Efectivo')),
                ('fk_pago_hist_dolar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.historicodolar', verbose_name='Historico Dolar')),
                ('fk_pago_punt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.puntos', verbose_name='Puntos')),
                ('fk_pago_tdc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.tarjetacredito', verbose_name='Tarjeta de Credito')),
                ('fk_pago_vent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name_plural': 'Pago',
            },
        ),
    ]
