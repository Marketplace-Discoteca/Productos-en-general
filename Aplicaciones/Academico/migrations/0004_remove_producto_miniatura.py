# Generated by Django 5.1.1 on 2024-09-27 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_producto_miniatura_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='miniatura',
        ),
    ]
