from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from contatos.models import Contato, Endereco, HistoricoContato, HistoricoEndereco

# Create your views here.


class DashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        total_contato = Contato.objects.count()
        total_atividades_contato = HistoricoContato.objects.count()
        total_endereco = Endereco.objects.count()
        total_atividades_endereco = HistoricoContato.objects.count()
        total_atividades = total_atividades_contato + total_atividades_endereco
        totais = [{
            'label': 'Contatos',
            'total': total_contato
        }, {
            'label': 'Atividades',
            'total': total_atividades
        }, {
            'label': 'Endereços',
            'total': total_endereco
        }]
        historicos_contatos = HistoricoContato.objects.all()[:5]
        return render(request, 'dashboard/index.html', {
            'totais': totais,
            'historicos_contatos': historicos_contatos
        })
