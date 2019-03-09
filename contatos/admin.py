from django.contrib import admin

from contatos.models import Contato, Endereco, HistoricoContato, HistoricoEndereco

admin.site.register(Contato)
admin.site.register(Endereco)
admin.site.register(HistoricoContato)
admin.site.register(HistoricoEndereco)
