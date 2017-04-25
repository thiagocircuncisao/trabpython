import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone

# Create your models here.


class Uf(models.Model):
    ufId = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50,verbose_name="Estado")

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name="Estado"
        verbose_name_plural="Estados"

class Muncipio(models.Model):
    municipioId = models.AutoField(primary_key=True)
    ufId = models.ForeignKey(Uf, 'ufId', verbose_name="Estado")
    descricao = models.CharField(max_length=255, verbose_name="Município")
    def __str__(self):
        return self.descricao

class ContaBancaria(models.Model):
    contaBancariaId = models.AutoField(primary_key=True)
    classificacao = models.CharField(max_length=18, verbose_name="Classificação")
    descricao = models.CharField(max_length=50)
    numeroAgencia = models.CharField(max_length=20, verbose_name="Agência")
    numeroConta = models.CharField(max_length=20, verbose_name="Conta")
    dataSaldoInicial = models.DateField()
    saldoIncial = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")
    caixa = models.CharField(max_length=1)
    banco = models.CharField(max_length=1)

    def __str__(self):
        return self.descricao

class PlanoContas(models.Model):
    planoContasId = models.AutoField(primary_key=True)
    contaCancariaId = models.ForeignKey(ContaBancaria,'contaBancariaId')
    classificacao = models.CharField(max_length=18)
    tipoConta = models.CharField(max_length=15)
    descricao = models.CharField(max_length=50)
    caixa = models.CharField(max_length=1)
    banco = models.CharField(max_length=1)
    cliente = models.CharField(max_length=1)
    fornecedor = models.CharField(max_length=1)
    entradaRecurso = models.CharField(max_length=1)
    saidaRecurso = models.CharField(max_length=1)

    def __str__(sef):
        return self.descricao

class Pessoa(models.Model):
    pessoaId =  models.IntegerField(primary_key=True)
    classificacao = models.CharField(max_length=18)
    indentificacao = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=50)
    ufId = models.ForeignKey(Uf, 'ufId', verbose_name="Estado")
    municipioID = models.ForeignKey(Muncipio, 'municipioId')
    cep = models.CharField(max_length=10)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=15)
    inscricaoEstadual =  models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)

class Empresa(models.Model):
    EmpresaId = models.IntegerField(primary_key=True)
    titularId = models.ForeignKey(PessoaJuridica, "pessoaId")
    razaoSocial = models.CharField(max_length=255)
    inscricaoEstadual =  models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=50)
    ufId = models.ForeignKey(Uf, 'ufId')
    municipioID = models.ForeignKey(Muncipio, 'municipioId')
    cep = models.CharField(max_length=10)

class FormaPagamento(models.Model):
    FormaPagamentoId = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

class Lancamentos(models.Model):
    lancamentosId = models.IntegerField(primary_key=True)
    tipoLancamento = models.CharField(max_length=1)
    numeroDocumento = models.CharField(max_length=20)
    dataVencimento = models.DateField()
    dataEmissao = models.DateField()
    valorTitulo = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")

class baixas(models.Model):
    baixasId = models.IntegerField(primary_key=True)
    lancamentosId = models.ForeignKey(Lancamentos,"lancamentosId")
