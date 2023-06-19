# Generated by Django 4.2.1 on 2023-05-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0014_remove_habitation_search_habi_adresse_392877_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitation',
            name='adresse',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='habitation',
            name='annee',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='habitation',
            name='energie',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='habitation',
            name='ges',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='habitation',
            name='surface',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='habitation',
            name='type_logement',
            field=models.TextField(default='', max_length=50),
        ),
    ]