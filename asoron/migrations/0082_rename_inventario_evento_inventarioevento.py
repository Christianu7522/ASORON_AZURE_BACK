# Generated by Django 4.2.7 on 2023-12-08 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0081_alter_inventario_evento_fk_inve_event_inve_tiend'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventario_Evento',
            new_name='InventarioEvento',
        ),
    ]
