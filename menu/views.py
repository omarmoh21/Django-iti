import json
import os
from django.shortcuts import render
from django.conf import settings


def menu_view(request):
    file_path = os.path.join(settings.BASE_DIR, 'menu', 'data', 'menu.json')

    with open(file_path) as f:
        items = json.load(f)

    search_query = request.GET.get('search')
    category_filter = request.GET.get('category')

    if search_query:
        items = [item for item in items if search_query.lower() in item['name'].lower()]

    if category_filter:
        items = [item for item in items if item['category'] == category_filter]

    context = {
        'items': items
    }

    return render(request, 'menu/menu.html', context)