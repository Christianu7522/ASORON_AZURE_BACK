# Generated by Django 4.2.7 on 2023-12-02 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0064_alter_asistencia_fk_asis_empl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correoelectronico',
            name='fk_mail_prov',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='asoron.proveedor'),
            preserve_default=False,
        ),
    ]
