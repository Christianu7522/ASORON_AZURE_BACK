# Generated by Django 4.2.7 on 2023-11-14 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0047_alter_clientejuridico_fk_clie_juri_lugar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificaciontipo',
            name='fk_clasi_tipo_tipo_ron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasi_tipo_tipo_ron', to='asoron.tiporon', verbose_name='Tipo Ron'),
        ),
    ]
