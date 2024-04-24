from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class DetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    def __str__(self):
        return self.name or ''
    
class CreateTaxModel(models.Model):
    tax_name = models.CharField(max_length=100)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tax_name}: {self.tax_amount}"

