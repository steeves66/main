# Generated by Django 5.0.2 on 2024-08-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bien_immobiliers', '0030_commodite_depositaire_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bien',
            name='commodités',
            field=models.ManyToManyField(related_name='biens', to='bien_immobiliers.commodite'),
        ),
    ]
