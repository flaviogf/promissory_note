from django.shortcuts import redirect, render
from django.views import View

from contatos.forms import ContatoForm, EnderecoForm
from contatos.models import Contato

# Create your views here.


class ListaContatoView(View):
    def get(self, request):
        contatos = Contato.objects.all()
        return render(request, 'contatos/index.html', {'contatos': contatos})


class CadastraContatoView(View):
    def get(self, request):
        contato_form = ContatoForm()
        endereco_form = EnderecoForm()
        return render(request, 'contatos/create.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })

    def post(self, request):
        contato_form = ContatoForm(request.POST or None)
        endereco_form = EnderecoForm(request.POST or None)

        if contato_form.is_valid() and endereco_form.is_valid():
            contato = contato_form.save()
            endereco = endereco_form.save(commit=False)
            endereco.contato = contato
            endereco.save()
            return redirect('contatos:list')

        return render(request, 'contatos/create.html', {
            'contato_form': contato_form,
            'endereco_form': endereco_form
        })
