from django.urls import path

from usuarios.views import LoginView, RegistarUsuarioView

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', RegistarUsuarioView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
