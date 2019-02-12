from django.shortcuts import render
from django.views import View

from contatos.models import Contato

# Create your views here.


class ListaContatoView(View):
    def get(self, request):
        contatos = Contato.objects.all()
        return render(request, 'contatos/index.html', {'contatos': contatos})
