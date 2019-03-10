from django.urls import path
from rest_framework.routers import SimpleRouter

from usuarios.views import LoginView, LogoutView, RegistarUsuarioView
from usuarios.viewsets import UsuarioViewSet

app_name = "usuarios"

router = SimpleRouter()
router.register(r"api/v2", UsuarioViewSet, base_name="api-v2")

urlpatterns = [
    path("registrar/", RegistarUsuarioView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
] + router.urls
