# Generated by Django 4.2.7 on 2023-11-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0046_alter_empleado_fk_empl_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientejuridico',
            name='fk_clie_juri_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asoron.lugar', verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='clientejuridico',
            name='fk_clie_juri_tipo_come',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asoron.tipocomercio', verbose_name='Tipo de Comercio'),
        ),
        migrations.AlterField(
            model_name='clientenatural',
            name='fk_clie_natu_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asoron.lugar', verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_empl_depa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asoron.departamento', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fk_prov_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asoron.lugar', verbose_name='Direccion'),
        ),
    ]
