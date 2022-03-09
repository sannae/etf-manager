from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Load all objects from database
etfs = ETF.objects.all()


def index(request):
    
    context = {
        'etfs': etfs,
    }

    return render(request, 'etf_manager/index.html', context)
