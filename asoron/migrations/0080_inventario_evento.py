# Generated by Django 4.2.7 on 2023-12-08 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0079_inventariotienda_historicoron'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario_Evento',
            fields=[
                ('inve_event_id', models.AutoField(primary_key=True, serialize=False, verbose_name='identificador')),
                ('inve_event_cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('fk_inve_event_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.evento', verbose_name='Evento')),
                ('fk_inve_event_inve_tiend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.inventariotienda', verbose_name='Inventario Tienda')),
            ],
            options={
                'verbose_name_plural': 'Inventario Evento',
                'unique_together': {('fk_inve_event_inve_tiend', 'fk_inve_event_event')},
            },
        ),
    ]
