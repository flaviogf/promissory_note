from django.urls import path

from usuarios.views import LoginView, LogoutView, RegistarUsuarioView

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', RegistarUsuarioView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
