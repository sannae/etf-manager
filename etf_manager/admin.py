from django.contrib import admin
from .models import *

# Customized
class ETFAdmin(admin.ModelAdmin):
    list_display = ('isin', 'ticker', 'value', 'currency', 'category')
    list_filter = ('category', 'currency', 'geography', 'sector')
    fields = (
        ('isin', 'ticker'),
        'description',
        ('size', 'value','distribution_policy'),
        ('currency', 'ter'),
        ('category', 'geography', 'sector'),
    )

# Standard models
admin.site.register(ETF, ETFAdmin)
admin.site.register(DistributionPolicy)
admin.site.register(Category)
admin.site.register(Geography)
admin.site.register(Sector)
admin.site.register(Order)
admin.site.register(Tag)

