import pandas as pd
from .models import Valeur
import os
import numpy as np
import requests

def is_number(s):
    try:
        if np.isnan(float(s)):
            return False
        else:
            return True
    except ValueError:
        return False

def create_values_from_csv():
    folder_path = 'search/csv/valeur/'  # Remplacez par le chemin de votre dossier

    # Créer une liste de tous les fichiers CSV dans le dossier
    csv_file = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    for csv in csv_file:
        chunk_iter = pd.read_csv(folder_path + csv, chunksize=10000, low_memory=False)
        for chunk_df in chunk_iter:
            values = []
            for index, row in chunk_df.iterrows():
                if is_number(row['code_postal']):
                    code_postal = str(int(float(row['code_postal'])))
                else:
                    code_postal = row['code_postal']
                adresse_numero = str(int(float(row['adresse_numero']))) if pd.notnull(row['adresse_numero']) else ''
                valeurs = Valeur(
                    adresse = adresse_numero + ' ' + str(row['adresse_nom_voie']).lower(),
                    fonciere=row['valeur_fonciere'],
                    date_transaction=row['date_mutation'],
                    code_postal=code_postal,
                )
                values.append(valeurs)
            Valeur.objects.bulk_create(values)
        print('Fichier valeur fonciere ' + csv + ' traité avec succès !')


def get_dpe_data(address=None, year=None, energie=None, audit=None, type=None, page=1):
    base_url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france/lines/"

    # Construire la requête en fonction des arguments fournis
    query_parts = []
    if address is not None and address != "":
        query_parts.append(f"geo_adresse:{address}")
    if year is not None and year != "":
        query_parts.append(f"annee_construction:{year}")
    if energie is not None and energie != "":
        query_parts.append(f"classe_consommation_energie:{energie}")
    if audit is not None and audit != "":
        query_parts.append(f"date_etablissement_dpe:{audit}")
    if type is not None and type != "":
        query_parts.append(f"tr002_type_batiment_description:{type}")
    query = " AND ".join(query_parts)

    params = {"qs": query, "page": page}
    response = requests.get(base_url, params=params)
    if response:
        data = response.json()
    else:
        data = None
    return data

def parse_data(data):
    results = data.get('results', [])
    parsed_results = []
    for result in results:
        parsed_result = {
            "date_audit": result.get('date_etablissement_dpe'),
            "annee_construction": result.get('annee_construction'),
            "classe_conso_energie": result.get('classe_consommation_energie'),
            "classe_ges": result.get('classe_estimation_ges'),
            "surface_habitable": result.get('surface_thermique_lot'),
            "type_logement": result.get('tr002_type_batiment_description'),
            "adresse": result.get('geo_adresse'),
        }
        parsed_results.append(parsed_result)
    return parsed_results
