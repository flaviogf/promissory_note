from django.urls import path

from contatos.views import ListaContatoView

app_name = 'contatos'

urlpatterns = [path('', ListaContatoView.as_view(), name='lista')]
