# Generated by Django 4.2.8 on 2023-12-22 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0111_alter_compra_compr_prove'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='compr_prove',
            new_name='fk_compr_prove',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='compr_tiend',
            new_name='fk_compr_tiend',
        ),
        migrations.RenameField(
            model_name='ventastatus',
            old_name='venta_stat_compr',
            new_name='fk_venta_stat_compr',
        ),
        migrations.RenameField(
            model_name='ventastatus',
            old_name='venta_stat_stat_pedi',
            new_name='fk_venta_stat_stat_pedi',
        ),
    ]
