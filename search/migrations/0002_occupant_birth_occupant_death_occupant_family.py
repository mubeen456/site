# Generated by Django 4.2 on 2023-04-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupant',
            name='birth',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='occupant',
            name='death',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='occupant',
            name='family',
            field=models.CharField(default='', max_length=50),
        ),
    ]
