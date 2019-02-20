from django.urls import path

from contas.views import ContasContatoView

app_name = 'contas'

urlpatterns = [
    path('contato/<uuid:contato_id>/',
         ContasContatoView.as_view(), name='contato-create')
]
