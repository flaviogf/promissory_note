from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from infra.utils import log_request
from usuarios.forms import LoginForm, RegistrarUsuarioForm

# Create your views here.


class RegistarUsuarioView(View):
    @method_decorator(log_request)
    def get(self, request):
        registrar_usuario_form = RegistrarUsuarioForm()
        return render(request, 'usuarios/register.html',
                      {'registrar_usuario_form': registrar_usuario_form})

    @method_decorator(log_request)
    def post(self, request):
        registrar_usuario_form = RegistrarUsuarioForm(request.POST)
        if registrar_usuario_form.is_valid():
            registrar_usuario_form.save()
            return redirect('usuarios:login')

        return render(request, 'usuarios/register.html',
                      {'registrar_usuario_form': registrar_usuario_form})


class LoginView(View):
    @method_decorator(log_request)
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'usuarios/login.html',
                      {'login_form': login_form})

    @method_decorator(log_request)
    def post(self, request):
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            url = request.GET.get('next', 'dashboard:index')
            usuario = login_form.get_user()
            login(request, usuario)
            return redirect(url)
        return render(request, 'usuarios/login.html',
                      {'login_form': login_form})


class LogoutView(View):
    @method_decorator(log_request)
    def get(self, request):
        logout(request)
        return redirect('usuarios:login')
