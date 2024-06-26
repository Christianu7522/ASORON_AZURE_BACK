# Generated by Django 4.2.7 on 2023-11-10 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0012_alter_sensacionron_fk_sens_ron_ron'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('mate_prima_id', models.AutoField(primary_key=True, serialize=False)),
                ('mate_prima_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrimaRon',
            fields=[
                ('mate_prima_ron_id', models.AutoField(primary_key=True, serialize=False)),
                ('fk_mate_prima_ron_mate_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.materiaprima')),
                ('fk_mate_prima_ron_ron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mate_prima_ron_ron', to='asoron.ron')),
            ],
            options={
                'unique_together': {('fk_mate_prima_ron_mate_prima', 'fk_mate_prima_ron_ron')},
            },
        ),
    ]
