# Generated by Django 5.0.6 on 2024-08-07 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bien_immobiliers', '0036_remove_bienpiece_nombre_bienmedia_piece'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bienpiece',
            old_name='interieur',
            new_name='commodites',
        ),
        migrations.RemoveField(
            model_name='bienmedia',
            name='nom',
        ),
    ]