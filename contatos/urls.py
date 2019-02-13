from django.urls import path

from contatos.views import CadastraContatoView, ListaContatoView

app_name = 'contatos'

urlpatterns = [
    path('', ListaContatoView.as_view(), name='list'),
    path('criar/', CadastraContatoView.as_view(), name='create'),
]
