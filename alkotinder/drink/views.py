from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello world!')


def drinks(request):
    return render(request, 'drink.html')
# Create your views here.
