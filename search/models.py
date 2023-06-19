from django.db import models

class Valeur(models.Model):
    adresse = models.CharField(max_length=50, default='')
    fonciere = models.CharField(max_length=50, default='')
    code_postal = models.CharField(max_length=50, default='')
    date_transaction = models.CharField(max_length=50, default='')
