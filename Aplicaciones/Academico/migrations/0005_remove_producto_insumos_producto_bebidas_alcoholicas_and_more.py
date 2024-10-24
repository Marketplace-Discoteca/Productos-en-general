# Generated by Django 5.1.1 on 2024-09-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0004_remove_producto_miniatura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='insumos',
        ),
        migrations.AddField(
            model_name='producto',
            name='bebidas_alcoholicas',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='mesas_adicionales_precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre_cliente',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='platos_a_la_carta',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='restricciones',
            field=models.TextField(blank=True),
        ),
    ]