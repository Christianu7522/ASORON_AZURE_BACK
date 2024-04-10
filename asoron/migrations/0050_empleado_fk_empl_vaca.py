# Generated by Django 4.2.7 on 2023-11-20 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0049_asistencia_beneficio_horario_salario_vacacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fk_empl_vaca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='asoron.vacacion', verbose_name='Vacacion'),
        ),
    ]
