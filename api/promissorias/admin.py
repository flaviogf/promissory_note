from django.contrib import admin

from api.promissorias.models import Promissoria


class PromissoriaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'valor')


admin.site.register(Promissoria, PromissoriaAdmin)
