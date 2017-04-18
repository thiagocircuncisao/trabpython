import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone

# Create your models here.

class ContaBancaria(models.Model):
    contabancariaid = models.IntegerField(primary_key=True)
    classificacao = models.CharField(max_length=18)
    descricao = models.CharField(max_length=50)
    numeroagencia = models.CharField(max_length=20)
    numeroconta = models.CharField(max_length=20)
    datasaldoinicial = models.DateField()
    saldoincial = models.MoneyField()
    caixa = models.CharField(max_length=1)
    banco = models.CharField(max_length=1)



class PlanoContas(models.Model):
    planocontasid = models.IntegerField(primary_key=True)
