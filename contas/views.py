from django.shortcuts import render
from django.views import View

# Create your views here.


class CadastroContaContatoView(View):
    def get(self, request, contato_id):
        return render(request, 'contas/contato/create.html')
