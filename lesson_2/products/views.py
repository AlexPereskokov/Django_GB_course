from django.shortcuts import render
import json


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
        'products': json.load(open("products/fixtures/products.json", encoding='utf-8')),
        'topics': [
            'Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'
        ]
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    context = {
        'title': 'Test Context',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6090'},
            {'name': 'Синяя куртка The North Face', 'price': '23725'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3390'},
        ]
    }
    return render(request, 'products/test-context.html', context)
