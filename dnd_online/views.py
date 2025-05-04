from django.shortcuts import render
from .models import Adventures
import random


adventures = Adventures.objects.all()

content = {
    'adventures': adventures,
}

def index(request):

    rnm_adventures = list(Adventures.objects.all())  # Получаем все объекты
    random_adventures = random.sample(rnm_adventures, min(3, len(rnm_adventures)))  # Выбираем случайные 3 объекта
    content['random_adventures'] = random_adventures

    return render(request, 'dnd_online/homePage.html', content)

def page_not_found(request, exeption):
    return render(request, '404.html')