# Generated by Django 4.2.8 on 2023-12-14 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0093_alter_clientejuridico_fk_clie_juri_lugar_fiscal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientenatural',
            name='fk_clie_natu_lugar',
            field=models.ForeignKey(limit_choices_to={'lugar_tipo': 'parroquia'}, on_delete=django.db.models.deletion.PROTECT, to='asoron.lugar', verbose_name='Direccion'),
        ),
    ]
