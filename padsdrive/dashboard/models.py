import email
from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Donor(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    second_name =models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    phone_number=models.CharField(max_length=100, null=True, blank=True  )
    donation_amount=MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    donation_description=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class PadDriveGroup(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    donation_amount=MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    contact_person=models.CharField(max_length=100, null=True, blank=True)
    phone_number=models.CharField(max_length=100)
    no_pads=models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.name