from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models import Sum, Count
from .models import *

# Load all objects from database
etfs = ETF.objects.all().order_by('isin')
orders = Order.objects.all()


# Home
def index(request):
    # https://stackoverflow.com/questions/45547674/how-to-execute-a-group-by-count-or-sum-in-django-orm
    
    grouped_shares = ETF.objects.annotate(order_count=Count('order'), order_quantity_sum=Sum('order__quantity'))

    """
    for etf in grouped_shares:
        print(etf.isin, etf.order_count, etf.order_quantity_sum)
    """

    context = { 'etfs': etfs, 'orders': orders, 'grouped_shares': grouped_shares }
    return render(request, 'etf_manager/index.html', context)

# ETF list view
class etf_list(ListView):
    model = ETF

# ETF detail view
class etf_detail(DetailView):
    model = ETF

class order_list(ListView):
    model = Order

class order_detail(DetailView):
    model = Order

