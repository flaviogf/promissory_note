from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from contas.models import Conta, HistoricoConta
from contatos.models import Contato, Endereco, HistoricoContato
from infra.decorators import log_request


class DashboardView(View):
    @method_decorator(log_request)
    @method_decorator(login_required)
    def get(self, request):
        total_contato = Contato.objects.filter(usuario=request.user).count()
        total_atividades_contato = HistoricoContato.objects.filter(
            contato__usuario=request.user
        ).count()
        total_contas = Conta.objects.filter(contato__usuario=request.user).count()
        total_atividades_conta = HistoricoConta.objects.filter(
            conta__contato__usuario=request.user
        ).count()
        total_atividades = total_atividades_contato + total_atividades_conta
        totais = [
            {"label": "Contatos", "total": total_contato},
            {"label": "Atividades", "total": total_atividades},
            {"label": "Contas", "total": total_contas},
        ]
        historicos_contatos = HistoricoContato.objects.filter(
            contato__usuario=request.user
        )[:5]
        historicos_contas = HistoricoConta.objects.filter(
            conta__contato__usuario=request.user
        )[:5]
        return render(
            request,
            "dashboard/index.html",
            {
                "totais": totais,
                "historicos_contatos": historicos_contatos,
                "historicos_contas": historicos_contas,
            },
        )
