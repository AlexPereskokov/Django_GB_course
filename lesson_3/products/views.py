from django.shortcuts import render
import json
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop Store',
        'description': 'Новые образы и лучшие бренды на GeekShop Store.'
                       'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% '
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог ',
        # 'products': json.load(open("products/fixtures/products.json", encoding='utf-8')),
        'products': Product.objects.all(),
        'topics': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
