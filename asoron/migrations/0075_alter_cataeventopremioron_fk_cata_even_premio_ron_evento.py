# Generated by Django 4.2.7 on 2023-12-07 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0074_alter_cataeventopremioron_fk_cata_even_premio_ron_evento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cataeventopremioron',
            name='fk_cata_even_premio_ron_evento',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='asoron.evento', verbose_name='Evento'),
        ),
    ]
