from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from contas.forms import ContaForm
from contas.models import Conta
from contatos.models import Contato
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
        return render(request, 'contas/contato/create.html', {
            'contato': contato,
            'conta_form': conta_form,
            'contas': contas
        })

    @method_decorator(log_request)
    @method_decorator(login_required)
    def post(self, request, contato_id):
        contato = get_object_or_404(
            Contato, usuario=request.user, contato_id=contato_id)
        conta_form = ContaForm(request.POST)

        if conta_form.is_valid():
            conta_form.save()
            url = reverse(
                'contas:contato-create', kwargs={'contato_id': contato_id})
            return redirect(url)

        contas = Conta.objects.filter(contato=contato)

        return render(request, 'contas/contato/create.html', {
            'contato': contato,
            'conta_form': conta_form,
            'contas': contas
        })
