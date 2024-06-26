# Generated by Django 4.2.7 on 2023-11-13 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0030_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComoServir',
            fields=[
                ('como_serv_id', models.AutoField(primary_key=True, serialize=False)),
                ('como_serv_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ComoServirRon',
            fields=[
                ('como_serv_ron_id', models.AutoField(primary_key=True, serialize=False)),
                ('como_serv_ron_descripcion', models.CharField(max_length=200)),
                ('fk_como_serv_ron_como_serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asoron.comoservir')),
                ('fk_como_serv_ron_ron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='como_serv_ron_ron', to='asoron.ron')),
            ],
            options={
                'verbose_name_plural': 'Como Servir Ron',
                'unique_together': {('fk_como_serv_ron_como_serv', 'fk_como_serv_ron_ron')},
            },
        ),
    ]
