# Generated by Django 5.0.6 on 2024-06-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficios', '0002_rename_empresas_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='Descuento',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
