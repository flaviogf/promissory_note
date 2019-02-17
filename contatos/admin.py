from django.contrib import admin

from contatos.models import AtividadeContato, Contato, Endereco

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'rua', 'bairro')


class AtividadeContatoAdmin(admin.ModelAdmin):
    list_display = ('mensagem', 'status_atual', 'atualizado_em')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(AtividadeContato, AtividadeContatoAdmin)
