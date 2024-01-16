from django.shortcuts import render
from django.http import HttpResponse
from time import ctime

# Create your views here.
def time(request):
    time1=ctime()
    return HttpResponse(f'Текущее время:{time1}')

def aboat(request):
    context = {
        'aboat': "Мы занимаемся програмированием и обучаем вас програмировать"
    }
    return render(request, 'aboat.html', context)

def index(request):
    context = {
        'title': "__ Главная страница ___",
        'description': "Описание",
        'jobs': ["Аристократ Ислам", "Астранафт Луналикая-Эльмира", "Пахатель Оля", "Дизайнер Толя"]
    }
    return render(request, "index.html", context)


def contact(request):
    context = {
        'title': "Это страница контакты",
        'phone': "0771244745",
        'instagram': "Username"
    }
    return render(request, 'contact.html', context)

def weather(request):
    context = {
        'weather': "Ясно(но не точно)"
    }
    return render(request, "weather.html", context)