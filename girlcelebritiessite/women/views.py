from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения Women')


def categories(request):
    return HttpResponse('<h1>Статьи по категориям.</h1>')
