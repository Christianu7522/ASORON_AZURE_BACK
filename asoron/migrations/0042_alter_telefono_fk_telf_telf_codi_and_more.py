# Generated by Django 4.2.7 on 2023-11-13 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0041_alter_barrilanejamiento_barr_anej_anos_barril_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='fk_telf_telf_codi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.telefonocodigo', verbose_name='Codigo de area'),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='telf_numero',
            field=models.CharField(max_length=7, verbose_name='Numero de telefono'),
        ),
    ]
