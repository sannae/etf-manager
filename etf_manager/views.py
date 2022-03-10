from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

# Load all objects from database
etfs = ETF.objects.all()

# Home
def index(request):
    context = { 'etfs': etfs, }
    return render(request, 'etf_manager/index.html', context)

# ETF list view
class etf_list(ListView):
    model = ETF

# ETF detail view
class etf_detail(DetailView):
    model = ETF