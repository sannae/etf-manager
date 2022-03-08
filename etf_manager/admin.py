from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ETF)
admin.site.register(DistributionPolicy)
admin.site.register(Category)
admin.site.register(Geography)
admin.site.register(Sector)
admin.site.register(Order)
admin.site.register(Tag)

