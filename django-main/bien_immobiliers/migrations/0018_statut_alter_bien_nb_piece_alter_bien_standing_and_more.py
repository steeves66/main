# Generated by Django 5.0.6 on 2024-07-22 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bien_immobiliers', '0017_localisationtype_remove_bien_commune_remove_bien_gps_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='bien',
            name='nb_piece',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='standing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bien_immobiliers.standing'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='superficie',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='superficie_habitable',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bien',
            name='type_bien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bien_immobiliers.bientype'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='type_maison',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bien_immobiliers.typemaison'),
        ),
        migrations.AlterField(
            model_name='bien',
            name='utilisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bien_immobiliers.utilisation'),
        ),
        migrations.AlterField(
            model_name='localisationtype',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bien',
            name='statut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bien_immobiliers.statut'),
        ),
    ]