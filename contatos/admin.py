from django.contrib import admin

from contatos.models import Contato, Endereco

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'rua', 'bairro')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
