"""Contains register-related models."""

from django.db import models

class Account(models.Model):
    """Represents an account where transactions occur."""
    name = models.CharField(max_length=50, unique=True)
    note = models.CharField(max_length=200, blank=True)

class MasterCategory(models.Model):
    """Represents a categorization for categories."""
    name = models.CharField(max_length=50, unique=True)

class Category(models.Model):
    """Represents a categorization for transactions."""
    name = models.CharField(max_length=50, unique=True)
    master_category = models.ForeignKey(MasterCategory, on_delete=models.SET_NULL, null=True)

class Payee(models.Model):
    """Represents an entity to/from which transactions are sent/received."""
    name = models.CharField(max_length=50, unique=True)

class Transaction(models.Model):
    """Represents an individual transaction."""
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    payee = models.ForeignKey(Payee, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    memo = models.CharField(max_length=200)
    outflow = models.DecimalField(max_digits=7, decimal_places=2)
    inflow = models.DecimalField(max_digits=7, decimal_places=2)
    cleared = models.BooleanField(default=False)
