from django.contrib import admin
from .models import *

# Customized
class ETFAdmin(admin.ModelAdmin):
    pass

# Standard models
admin.site.register(ETF, ETFAdmin)
admin.site.register(DistributionPolicy)
admin.site.register(Category)
admin.site.register(Geography)
admin.site.register(Sector)
admin.site.register(Order)
admin.site.register(Tag)

