from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from contatos.forms import ContatoForm, EnderecoForm
from contatos.models import AtividadeContato, Contato
from infra.utils import log

# Create your views here.


class ListaContatoView(View):
    @method_decorator(log('contatos:list'))
    @method_decorator(login_required)
    def get(self, request):
        contatos = Contato.objects.filter(usuario=request.user)
        return render(request, 'contatos/index.html', {'contatos': contatos})


class CadastraContatoView(View):
    @method_decorator(log('contatos:create'))
    @method_decorator(login_required)
    def get(self, request):
        contato_form = ContatoForm()
        endereco_form = EnderecoForm()
        return render(request, 'contatos/create.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })

    @method_decorator(log('contatos:create'))
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
            AtividadeContato.objects.create(
                mensagem=f'Contato {contato.nome} foi criado',
                status_atual=contato.__dict__)
            return redirect('contatos:list')

        return render(request, 'contatos/create.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })


class EditaContatoView(View):
    @method_decorator(log('contatos:edit'))
    @method_decorator(login_required)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user)
        contato_form = ContatoForm(instance=contato)
        endereco_form = EnderecoForm(instance=contato.endereco)
        return render(request, 'contatos/edit.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })

    @method_decorator(log('contatos:edit'))
    @method_decorator(login_required)
    def post(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user)
        contato_form = ContatoForm(request.POST, instance=contato)
        endereco_form = EnderecoForm(request.POST, instance=contato.endereco)

        if contato_form.is_valid() and endereco_form.is_valid():
            novo_contato = contato_form.save()
            endereco_form.save()
            AtividadeContato.objects.create(
                mensagem=f'Contato {contato.nome} foi editado',
                status_atual=novo_contato.__dict__,
                status_anterior=contato.__dict__)
            return redirect('contatos:list')

        return render(request, 'contatos/edit.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })


class DeletaContatoView(View):
    @method_decorator(log('contatos:delete'))
    @method_decorator(login_required)
    def get(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user)
        contato_form = ContatoForm(instance=contato)
        endereco_form = EnderecoForm(instance=contato.endereco)
        return render(request, 'contatos/delete.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })

    @method_decorator(log('contatos:delete'))
    @method_decorator(login_required)
    def post(self, request, contato_id):
        contato = get_object_or_404(
            Contato, contato_id=contato_id, usuario=request.user)
        contato.delete()
        AtividadeContato.objects.create(
            mensagem=f'Contato {contato.nome} foi deletado',
            status_atual=None,
            status_anterior=contato.__dict__)
        return redirect('contatos:list')
