from winsound import PlaySound
from django.shortcuts import render
import random

def index(request):
    pla = random.randint(0, 30)
    plb = random.randint(0, 30)
    plmo = titkos(pla, plb)
    template = 'index.html'
    context = {
        'pla':pla, 
        'plb':plb, 
        'plmo':plmo,
        'fela':random.randint(0, 30),
        'felb':random.randint(0, 30),
    }
    if request.method == "POST":
        titkos(int(request.POST['regifela']), int(request.POST['regifelb'])==int(request.POST['felmo']))
    return render(request, template, context)

def titkos(a, b):
    return 2*a+b
