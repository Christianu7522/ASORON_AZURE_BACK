# Generated by Django 4.2.7 on 2023-11-11 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0026_alter_ron_fk_ron_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ron',
            name='fk_ron_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ron_color', to='asoron.color'),
        ),
        migrations.AlterField(
            model_name='ron',
            name='fk_ron_grado_alco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ron_grado_alcohol', to='asoron.gradoalcohol'),
        ),
        migrations.AlterField(
            model_name='ron',
            name='fk_ron_prove',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ron_proveedor', to='asoron.proveedor'),
        ),
    ]
