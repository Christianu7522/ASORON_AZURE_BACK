# Generated by Django 4.2.7 on 2023-11-10 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0015_alter_empleado_empl_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='empl_apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empl_cedula_identidad',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empl_nombre',
            field=models.CharField(max_length=50),
        ),
    ]
