from django.shortcuts import render
from .utils import get_dpe_data, parse_data
from math import ceil
import pandas as pd
from .models import Valeur

def search_view(request):
    adresse = request.GET.get('adress', '')
    annee = request.GET.get('annee', '')
    energie = request.GET.get('energie', '')
    audit = request.GET.get('audit', '')
    type = request.GET.get('type', '')
    page = int(request.GET.get('page', 1))

    data = get_dpe_data(adresse, annee, energie, audit, type, page)

    total_results = data.get('total', 0)
    total_pages = ceil(total_results / 12)

    if data:
        habitations = parse_data(data)

    else:
        habitations = []

    return render(request, 'search/results.html', {'results': habitations, 'page': page, 'total_pages': total_pages, 'total_results': total_results})
