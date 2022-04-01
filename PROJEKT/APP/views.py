import re
from winsound import PlaySound
from django.shortcuts import render
import random

def index(request):
    pla = random.randint(0, 30)
    plb = random.randint(0, 30)
    fela = random.randint(0, 30)
    felb = random.randint(0, 30)
    plmo = titkos(pla, plb)
    template = 'index.html'
    context = {
        'pla':pla, 
        'plb':plb, 
        'plmo':plmo,
        'fela':fela,
        'felb':felb,
    }
    if request.method == "POST":
        regifela = int(request.POST['regifela'])
        regifelb = int(request.POST['regifelb'])
        regifelmo_user_szerint = int(request.POST['felmo'])
        regifelmo_valojaban = titkos(regifela, regifelb)
        #print(regifela)
        #print(regifelb)
        #print(regifelmo_user_szerint)
        #print(regifelmo_valojaban)
        context['volt_valasz'] = True
        context['helyes'] = regifelmo_user_szerint == regifelmo_valojaban
    return render(request, template, context)

def titkos(a, b):
    return 2*a+b
