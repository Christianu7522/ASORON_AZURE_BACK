# Generated by Django 4.2.7 on 2023-11-11 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0028_clientejuridico_fk_clie_juri_lugar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientejuridico',
            name='fk_clie_juri_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.lugar'),
        ),
        migrations.AlterField(
            model_name='clientenatural',
            name='fk_clie_natu_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.lugar'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_empl_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.lugar'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fk_prov_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.lugar'),
        ),
    ]
