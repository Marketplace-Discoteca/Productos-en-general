# Generated by Django 5.1.1 on 2024-10-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0006_remove_producto_bebidas_alcoholicas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
