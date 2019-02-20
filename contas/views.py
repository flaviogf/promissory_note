from django.shortcuts import render, get_object_or_404
from django.views import View
from contas.forms import ContaForm

from contatos.models import Contato
from contas.models import Conta
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from infra.utils import log_request

# Create your views here.


class ContasContatoView(View):
    @method_decorator(log_request)
    @method_decorator(login_required)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user)
        contas = Conta.objects.filter(contato=contato)
        conta_form = ContaForm(initial={'contato': contato.contato_id})
        return render(request, 'contas/contato/create.html', {'contato': contato, 'conta_form': conta_form, 'contas': contas})
