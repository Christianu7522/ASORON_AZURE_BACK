# Generated by Django 4.2.8 on 2024-01-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0139_remove_venta_fk_vent_empl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacion',
            name='noti_descripcion',
            field=models.CharField(max_length=1500, verbose_name='Descripcion'),
        ),
    ]
