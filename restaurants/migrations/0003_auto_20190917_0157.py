# Generated by Django 2.1.7 on 2019-09-17 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20190917_0147'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImagenesEstabecimiento',
            new_name='ImagenesEstablecimiento',
        ),
        migrations.RenameField(
            model_name='imagenesestablecimiento',
            old_name='imagenes',
            new_name='imagen',
        ),
    ]
