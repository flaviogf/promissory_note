from django.contrib import admin

from contatos.models import Contato, Endereco, HistoricoContato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'rua', 'bairro')


class HistoricoContatoAdmin(admin.ModelAdmin):
    list_display = ('contato', 'nome', 'email', 'telefone', 'atualizado_em')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(HistoricoContato, HistoricoContatoAdmin)
