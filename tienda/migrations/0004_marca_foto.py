# Generated by Django 4.2.1 on 2023-11-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_marca_remoto_remove_producto_distribuidor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='foto',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
