# Generated by Django 4.2 on 2023-04-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_occupant_birth_occupant_death_occupant_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupant',
            name='pdf',
            field=models.CharField(default='', max_length=100),
        ),
    ]