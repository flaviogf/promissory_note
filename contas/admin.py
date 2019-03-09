from django.contrib import admin

from contas.models import Conta, HistoricoConta


class ContaAdmin(admin.ModelAdmin):
    list_display = ("valor", "data_recebimento_esperado")


class HistoricoContaAdmin(admin.ModelAdmin):
    list_display = ("conta", "valor", "data_recebimento_esperado")


admin.site.register(Conta, ContaAdmin)
admin.site.register(HistoricoConta, HistoricoContaAdmin)
