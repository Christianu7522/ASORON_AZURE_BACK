# Generated by Django 4.2.7 on 2023-11-11 14:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0029_alter_clientejuridico_fk_clie_juri_lugar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
    ]
