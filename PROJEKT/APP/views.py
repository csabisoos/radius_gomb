from django.shortcuts import render
from random import randint

def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)
