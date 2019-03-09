from django.contrib import admin

from contas.models import Conta, HistoricoConta

admin.site.register(Conta)
admin.site.register(HistoricoConta)
