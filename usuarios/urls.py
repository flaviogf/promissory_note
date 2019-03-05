from django.urls import path

from usuarios.views import LoginView, LogoutView, RegistarUsuarioView
from usuarios.api import UsuarioAPIView, LoginAPIView

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', RegistarUsuarioView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/', UsuarioAPIView.as_view(), name='usuarios_api_v1'),
    path('api/v1/login', LoginAPIView.as_view(), name='usuarios_api_v1_login'),
]
