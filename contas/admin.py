from django.contrib import admin
from contas.models import Conta

# Register your models here.


class ContaAdmin(admin.ModelAdmin):
    list_display = ('contato', 'valor', 'data_recebimento_esperado')


admin.site.register(Conta, ContaAdmin)
