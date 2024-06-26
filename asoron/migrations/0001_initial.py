# Generated by Django 4.2.7 on 2023-11-09 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionRon',
            fields=[
                ('clasi_ron_id', models.AutoField(primary_key=True, serialize=False)),
                ('clasi_ron_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClasificacionTipo',
            fields=[
                ('clasi_tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('fk_clasi_tipo_clasi_ron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasi_tipo_ron', to='asoron.clasificacionron')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteJuridico',
            fields=[
                ('clie_juri_id', models.AutoField(primary_key=True, serialize=False)),
                ('clie_juri_rif', models.CharField(max_length=10)),
                ('clie_juri_denominacion_comercial', models.CharField(max_length=50)),
                ('clie_juri_razon_social', models.CharField(max_length=50)),
                ('clie_juri_pagina_web', models.CharField(blank=True, max_length=50, null=True)),
                ('clie_juri_capital_disponible', models.PositiveIntegerField(default=0)),
                ('clie_juri_direccion_fisica', models.CharField(max_length=200)),
                ('clie_juri_direccion_fiscal', models.CharField(max_length=200)),
                ('clie_juri_puntos', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteNatural',
            fields=[
                ('clie_natu_id', models.AutoField(primary_key=True, serialize=False)),
                ('clie_natu_rif', models.CharField(max_length=10)),
                ('clie_natu_cedula_identidad', models.CharField(max_length=10)),
                ('clie_natu_nombre', models.CharField(max_length=50)),
                ('clie_natu_apellido', models.CharField(max_length=50)),
                ('clie_natu_segundo_nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('clie_natu_segundo_apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('clie_natu_direccion_habitacion', models.CharField(max_length=200)),
                ('clie_natu_puntos', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('depa_id', models.AutoField(primary_key=True, serialize=False)),
                ('depa_nombre', models.CharField(max_length=50)),
                ('depa_descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TelefonoCodigo',
            fields=[
                ('telf_cod_id', models.AutoField(primary_key=True, serialize=False)),
                ('telf_cod_codigo', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='TipoComercio',
            fields=[
                ('tipo_comer_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_comer_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRon',
            fields=[
                ('tipo_ron_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_ron_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('telf_id', models.AutoField(primary_key=True, serialize=False)),
                ('telf_numero', models.CharField(max_length=7)),
                ('fk_telf_clie_juri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clie_juri_telf', to='asoron.clientejuridico')),
                ('fk_telf_clie_natu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clie_natu_telf', to='asoron.clientenatural')),
                ('fk_telf_telf_codi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.telefonocodigo')),
            ],
        ),
        migrations.CreateModel(
            name='Ron',
            fields=[
                ('ron_id', models.AutoField(primary_key=True, serialize=False)),
                ('ron_nombre', models.CharField(max_length=50)),
                ('ron_descripcion', models.CharField(max_length=200)),
                ('fk_ron_clasi_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.clasificaciontipo')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('img_url', models.ImageField(upload_to='store/images')),
                ('fk_img_ron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ron_images', to='asoron.ron')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empl_id', models.AutoField(primary_key=True, serialize=False)),
                ('empl_direccion', models.CharField(max_length=200)),
                ('fk_empl_depa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.departamento')),
            ],
        ),
        migrations.AddField(
            model_name='clientejuridico',
            name='fk_clie_juri_tipo_come',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.tipocomercio'),
        ),
        migrations.AddField(
            model_name='clasificaciontipo',
            name='fk_clasi_tipo_tipo_ron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasi_tipo_ron', to='asoron.tiporon'),
        ),
        migrations.AlterUniqueTogether(
            name='clasificaciontipo',
            unique_together={('fk_clasi_tipo_clasi_ron', 'fk_clasi_tipo_tipo_ron')},
        ),
    ]
