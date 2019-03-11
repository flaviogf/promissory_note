from django.urls import path
from rest_framework.routers import SimpleRouter

from contas.views import ContasContatoRecebeView, ContasContatoView
from contas.viewsets import ContaViewSet

app_name = "contas"

router = SimpleRouter()
router.register("api/v2", ContaViewSet, base_name="api-v2")

urlpatterns = [
    path(
        "contato/<uuid:contato_id>/", ContasContatoView.as_view(), name="contato-create"
    ),
    path(
        "contato/<uuid:contato_id>/conta/<uuid:conta_id>/",
        ContasContatoRecebeView.as_view(),
        name="contato-recebe",
    ),
] + router.urls
