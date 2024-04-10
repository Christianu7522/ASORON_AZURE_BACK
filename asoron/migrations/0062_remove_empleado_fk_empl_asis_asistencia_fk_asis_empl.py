# Generated by Django 4.2.7 on 2023-12-02 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0061_alter_clientejuridico_fk_clie_juri_lugar_fiscal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='fk_empl_asis',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='fk_asis_empl',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='asoron.empleado', verbose_name='Empleado'),
        ),
    ]
