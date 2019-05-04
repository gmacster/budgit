from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=50, unique=True)
    note = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Payee(models.Model):
    name = models.CharField(max_length=50)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    payee = models.ForeignKey(Payee, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    memo = models.CharField(max_length=200)
    outflow = models.DecimalField(max_digits=7, decimal_places=2)
    inflow = models.DecimalField(max_digits=7, decimal_places=2)
    cleared = models.BooleanField(default=False)
