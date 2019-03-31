from django.contrib import admin

from api.emitentes.models import Emitente


class EmitenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Emitente, EmitenteAdmin)
