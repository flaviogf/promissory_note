from django.contrib import admin

from api.beneficiarios.models import Beneficiario


class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Beneficiario, BeneficiarioAdmin)
