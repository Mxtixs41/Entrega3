# Generated by Django 5.0.6 on 2024-06-19 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veranum', '0003_reserva_tipo_habitacion_delete_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='id_habitacion',
            field=models.ForeignKey(db_column='IDHABITACION', default=12, on_delete=django.db.models.deletion.CASCADE, to='Veranum.tipo_habitacion'),
            preserve_default=False,
        ),
    ]
