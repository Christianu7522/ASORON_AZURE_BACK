# Generated by Django 4.2.7 on 2023-11-10 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0009_barrilanejamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_nombre', models.CharField(max_length=50)),
                ('color_descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GradoAlcohol',
            fields=[
                ('grad_alco_id', models.AutoField(primary_key=True, serialize=False)),
                ('grad_alco_porcentaje_alcohol', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensacion',
            fields=[
                ('sens_id', models.AutoField(primary_key=True, serialize=False)),
                ('sens_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SensacionRon',
            fields=[
                ('sens_ron_id', models.AutoField(primary_key=True, serialize=False)),
                ('fk_sens_ron_ron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.ron')),
                ('fk_sens_ron_sens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.sensacion')),
            ],
            options={
                'unique_together': {('fk_sens_ron_sens', 'fk_sens_ron_ron')},
            },
        ),
    ]
