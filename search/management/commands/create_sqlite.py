from django.core.management.base import BaseCommand
from ...models import Valeur
from ...utils import create_values_from_csv

class Command(BaseCommand):
    help = "Crée une base de données SQLite à partir d'un DataFrame"

    def handle(self, *args, **options):
        Valeur.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Base de données SQLite vidée avec succès'))
        create_values_from_csv()
        self.stdout.write(self.style.SUCCESS('Base de données SQLite créée avec succès'))
