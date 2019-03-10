from django.urls import path
from rest_framework.routers import SimpleRouter

from contatos.views import (
    CadastraContatoView,
    DeletaContatoView,
    EditaContatoView,
    ListaContatoView,
)
from contatos.viewsets import ContatoViewSet

app_name = "contatos"

router = SimpleRouter()
router.register(r"api/v2", ContatoViewSet, base_name="api-v2")

urlpatterns = [
    path("", ListaContatoView.as_view(), name="list"),
    path("criar/", CadastraContatoView.as_view(), name="create"),
    path("<uuid:contato_id>/edita/", EditaContatoView.as_view(), name="edit"),
    path("<uuid:contato_id>/deleta/", DeletaContatoView.as_view(), name="delete"),
] + router.urls
