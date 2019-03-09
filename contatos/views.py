from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from contatos.forms import ContatoForm, EnderecoForm
from contatos.models import Contato
from infra.decorators import log_request


class ListaContatoView(View):
    @method_decorator(log_request)
    @method_decorator(login_required)
    def get(self, request):
        contatos = Contato.objects.filter(usuario=request.user)
        return render(request, "contatos/index.html", {"contatos": contatos})


class CadastraContatoView(View):
    @method_decorator(log_request)
    @method_decorator(login_required)
    def get(self, request):
        contato_form = ContatoForm()
        endereco_form = EnderecoForm()
        return render(
            request,
            "contatos/create.html",
            {"contato_form": contato_form, "endereco_form": endereco_form},
        )

    @method_decorator(log_request)
    @method_decorator(login_required)
    def post(self, request):
        contato_form = ContatoForm(request.POST or None)
        endereco_form = EnderecoForm(request.POST or None)

        if contato_form.is_valid() and endereco_form.is_valid():
            contato = contato_form.save(commit=False)
            endereco = endereco_form.save(commit=False)
            contato.usuario = request.user
            contato.save()
            endereco.contato = contato
            endereco.save()
            return redirect("contatos:list")

        return render(
            request,
            "contatos/create.html",
            {"contato_form": contato_form, "endereco_form": endereco_form},
        )


class EditaContatoView(View):
    @method_decorator(log_request)
    @method_decorator(login_required)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user
        )
        contato_form = ContatoForm(instance=contato)
        endereco_form = EnderecoForm(instance=contato.endereco)
        return render(
            request,
            "contatos/edit.html",
            {"contato_form": contato_form, "endereco_form": endereco_form},
        )

    @method_decorator(log_request)
    @method_decorator(login_required)
    def post(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user
        )
        contato_form = ContatoForm(request.POST, instance=contato)
        endereco_form = EnderecoForm(request.POST, instance=contato.endereco)

        if contato_form.is_valid() and endereco_form.is_valid():
            contato_form.save()
            endereco_form.save()
            return redirect("contatos:list")

        return render(
            request,
            "contatos/edit.html",
            {"contato_form": contato_form, "endereco_form": endereco_form},
        )


class DeletaContatoView(View):
    @method_decorator(log_request)
    @method_decorator(login_required)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user
        )
        contato_form = ContatoForm(instance=contato)
        endereco_form = EnderecoForm(instance=contato.endereco)
        return render(
            request,
            "contatos/delete.html",
            {"contato_form": contato_form, "endereco_form": endereco_form},
        )

    @method_decorator(log_request)
    @method_decorator(login_required)
    def post(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user
        )
        contato.delete()
        return redirect("contatos:list")
