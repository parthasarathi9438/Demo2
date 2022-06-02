from os import P_NOWAIT
from django.db import models

class Product(models.Model):
    pno = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()