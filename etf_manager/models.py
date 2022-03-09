import uuid
from django.db import models

# ETF identified by ISIN code
class ETF(models.Model):
    isin = models.CharField(max_length=12, primary_key=True, help_text='Enter ETF ISIN')
    ticker = models.CharField(max_length=10, help_text='Enter ETF Ticker')
    description = models.CharField(max_length=200, help_text='Enter a description', default='',blank=True)
    size = models.IntegerField(help_text='Enter ETF size')
    value = models.FloatField(help_text='Enter ETF current value')

    CURRENCIES = (
        ('EUR', 'Euro'),
        ('USD', 'United States Dollars'),
        ('JPY', 'Japan Yen'),
    )

    currency = models.CharField(max_length=3, choices=CURRENCIES, help_text='Select ETF Currency')
    distribution_policy = models.ForeignKey('DistributionPolicy', on_delete=models.PROTECT, help_text='Select ETF distribution policy')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, help_text='Select ETF Category')
    geography = models.ForeignKey('Geography', on_delete=models.PROTECT, help_text='Select ETF Geography')
    sector = models.ForeignKey('Sector', on_delete=models.PROTECT, help_text='Select ETF Sector')
    ter = models.FloatField(help_text='Enter ETF TER')
    location = models.CharField(max_length=50, help_text='Enter ETF location')
    manager = models.CharField(max_length=100, help_text='Enter ETF manager')
    tags = models.ManyToManyField('Tag', help_text='Select ETF tags')

    class Meta:
       ordering = ['category', 'isin']     

    # Returns the url to access a particular instance of the model
    def get_absolute_url(self):
        return reverse('etf-detail', args=[str(self.id)])

    def __str__(self):
        return self.isin


# Distribution policies (distribution 3mo, distribution 6mo, accumulation, etc.)
class DistributionPolicy(models.Model):
    description = models.CharField(max_length=20, help_text='Enter the distribution policy')

    class Meta:
        verbose_name_plural = "Distribution Policies"

    def __str__(self):
        return self.description    

# Categories (stocks, bonds, etc.)
class Category(models.Model):
    description = models.CharField(max_length=20, help_text='Enter the category')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.description

# Geographies (Europe, USA, Emerging Markets, etc.)
class Geography(models.Model):
    description = models.CharField(max_length=20, help_text='Enter the geography')

    class Meta:
        verbose_name_plural = "Geographies"

    def __str__(self):
        return self.description

# Economic sector (Energy, Financial, Healthcare, etc.)
class Sector(models.Model):
    description = models.CharField(max_length=20, help_text='Enter the economic sector')

    def __str__(self):
        return self.description

# Purchasing order
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text='Unique ID for this order')
    etf = models.ForeignKey(ETF, on_delete=models.PROTECT, help_text='Select the ETF')
    quantity = models.IntegerField(help_text='Enter the quantity')
    price = models.FloatField(help_text='Enter the current price')

    TRADING_PLATFORMS = (
        ('DEG', 'Degiro'),
        ('ING', 'ING Direct'),
    )

    trading_platform = models.CharField(max_length=3, choices=TRADING_PLATFORMS, help_text='Select the trading platform')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields=['updated_at', 'etf']),
        ]

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self):
        return self.quantity + ' ' + self.etf.description + ' at ' + str(self.price) + ' ' + self.etf.currency + ' on ' + self.trading_platform.name

# Just tags
class Tag(models.Model):
    description = models.CharField(max_length=50, help_text='Enter the tag')

    def __str__(self):
        return self.description