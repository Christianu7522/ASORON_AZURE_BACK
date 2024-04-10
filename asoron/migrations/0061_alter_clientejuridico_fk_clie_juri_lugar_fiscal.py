# Generated by Django 4.2.7 on 2023-12-02 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0060_remove_clientejuridico_fk_clie_juri_lugar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientejuridico',
            name='fk_clie_juri_lugar_fiscal',
            field=models.ForeignKey(limit_choices_to={'lugar_tipo': 'Parroquia'}, on_delete=django.db.models.deletion.PROTECT, related_name='clie_juri_lugar_fiscal', to='asoron.lugar', verbose_name='Direccion Fiscal Geografica'),
        ),
    ]
