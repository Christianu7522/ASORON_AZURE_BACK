# Generated by Django 4.2.7 on 2023-12-06 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0073_alter_notacata_fk_nota_cata_cata_even_premio_ron'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cataeventopremioron',
            name='fk_cata_even_premio_ron_evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.evento', verbose_name='Evento'),
        ),
        migrations.AlterField(
            model_name='cataeventopremioron',
            name='fk_cata_even_premio_ron_premio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.premio', verbose_name='Premio'),
        ),
    ]
