from django.contrib import admin
from .models import Uf
from .models import Muncipio
from .models import PessoaFisica
from .models import PessoaJuridica
from .models import ContaBancaria
from .models import PlanoContas

# Register your models here.
admin.site.register(Uf)
admin.site.register(Muncipio)
admin.site.register(PessoaJuridica)
admin.site.register(ContaBancaria)
class PlanoContasAdmin(admin.ModelAdmin):
    fields = ['tipoConta', 'classificacao']

admin.site.register(PlanoContas, PlanoContasAdmin)
