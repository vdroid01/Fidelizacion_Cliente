# Generated by Django 5.0.6 on 2024-06-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_rename_apellido_materno_cliente_apellido_materno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=80, null=True),
        ),
    ]
