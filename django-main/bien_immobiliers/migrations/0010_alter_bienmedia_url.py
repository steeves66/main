# Generated by Django 5.0.6 on 2024-07-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bien_immobiliers', '0009_depositairecontact_valeur_alter_depositaire_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienmedia',
            name='url',
            field=models.ImageField(upload_to='medias'),
        ),
    ]