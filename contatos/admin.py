from django.contrib import admin

from contatos.models import Contato, Endereco

# Register your models here.

admin.site.register(Contato)
admin.site.register(Endereco)
