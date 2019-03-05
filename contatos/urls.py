from django.urls import path

from contatos.views import CadastraContatoView, DeletaContatoView, EditaContatoView, ListaContatoView
from contatos.api import ContatoAPIView

app_name = 'contatos'

urlpatterns = [
    path('', ListaContatoView.as_view(), name='list'),
    path('criar/', CadastraContatoView.as_view(), name='create'),
    path('<uuid:contato_id>/edita/', EditaContatoView.as_view(), name='edit'),
    path(
        '<uuid:contato_id>/deleta/',
        DeletaContatoView.as_view(),
        name='delete'),
    path('api/v1/<uuid:contato_id>/', ContatoAPIView.as_view(), name='contatos_api_v1'),
]
