from django.db import models

class Transaction(models.Model):
    account = models.CharField()