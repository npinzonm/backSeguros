# Generated by Django 4.2.16 on 2024-11-25 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_usuario_vehiculo_poliza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='identificacion_cliente',
        ),
        migrations.DeleteModel(
            name='Poliza',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
