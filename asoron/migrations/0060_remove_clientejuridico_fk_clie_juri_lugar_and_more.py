# Generated by Django 4.2.7 on 2023-12-02 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0059_asistencia_asis_fecha_empleado_fk_empl_asis_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientejuridico',
            name='fk_clie_juri_lugar',
        ),
        migrations.AddField(
            model_name='clientejuridico',
            name='fk_clie_juri_lugar_fiscal',
            field=models.ForeignKey(default=7, limit_choices_to={'lugar_tipo': 'Parroquia'}, on_delete=django.db.models.deletion.PROTECT, related_name='clie_juri_lugar_fiscal', to='asoron.lugar', verbose_name='Direccion Fiscal Geografica'),
        ),
        migrations.AddField(
            model_name='clientejuridico',
            name='fk_clie_juri_lugar_fisica',
            field=models.ForeignKey(default=7, limit_choices_to={'lugar_tipo': 'Parroquia'}, on_delete=django.db.models.deletion.PROTECT, to='asoron.lugar', verbose_name='Direccion Fisica Geografica'),
            preserve_default=False,
        ),
    ]
