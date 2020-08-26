from django.db import models

# Create your models here.

class Statement(models.Model):
    date = models.DateField(auto_now=False)
    description = models.CharField(max_length=500, null=True)
    debit = models.FloatField(null=True, blank=True, default=None)
    credit = models.FloatField(null=True, blank=True, default=None)
    balance = models.FloatField(null=True, blank=True, default=None)
    category = models.CharField(max_length=100,null=True)
    
