from django.urls import path

from contas.views import CadastroContaContatoView

app_name = 'contas'

urlpatterns = [
    path('contato/<uuid:contato_id>/',
         CadastroContaContatoView.as_view(), name='contato-create')
]
