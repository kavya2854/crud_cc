from django.db import models
# Create your models here.
class Country(models.Model):
    countryid = models.IntegerField(primary_key = True)
    countryname = models.CharField(max_length = 100)
    currency = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.countryname,self.currency
class Capital(models.Model):
    capitalid = models.IntegerField(primary_key = True)
    capitalname = models.CharField(max_length = 100)
    countryid = models.OneToOneField(Country,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.capitalname