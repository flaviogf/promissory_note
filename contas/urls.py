from django.urls import path

from contas.views import ContasContatoRecebeView, ContasContatoView

app_name = 'contas'

urlpatterns = [
    path(
        'contato/<uuid:contato_id>/',
        ContasContatoView.as_view(),
        name='contato-create'),
    path(
        'contato/<uuid:contato_id>/conta/<uuid:conta_id>/',
        ContasContatoRecebeView.as_view(),
        name='contato-recebe'),
]
