# Generated by Django 4.2.8 on 2023-12-19 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0106_alter_clientenatural_clie_natu_cedula_identidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientejuridico',
            name='clie_juri_rif',
            field=models.CharField(max_length=10, unique=True, verbose_name='RIF'),
        ),
    ]
