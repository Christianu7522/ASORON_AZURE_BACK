# Generated by Django 4.2.7 on 2023-11-09 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0005_remove_anejamiento_calidad_agua_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='ron',
            name='fk_ron_anej',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asoron.anejamiento'),
        ),
        migrations.AlterField(
            model_name='anejamiento',
            name='fk_anej_meto_dest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anej_meto_dest', to='asoron.metododestilacion'),
        ),
        migrations.AlterField(
            model_name='anejamiento',
            name='fk_anej_meto_ferm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anej_meto_ferm', to='asoron.metodofermentacion'),
        ),
    ]
