from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from usuarios.forms import LoginForm, RegistrarUsuarioForm

# Create your views here.


class RegistarUsuarioView(View):
    def get(self, request):
        registrar_usuario_form = RegistrarUsuarioForm()
        return render(request, 'usuarios/register.html',
                      {'registrar_usuario_form': registrar_usuario_form})

    def post(self, request):
        registrar_usuario_form = RegistrarUsuarioForm(request.POST)
        if registrar_usuario_form.is_valid():
            registrar_usuario_form.save()
            return redirect('usuarios:login')

        return render(request, 'usuarios/register.html',
                      {'registrar_usuario_form': registrar_usuario_form})


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'usuarios/login.html',
                      {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            usuario = login_form.get_user()
            login(request, usuario)
            return redirect('contatos:list')
        return render(request, 'usuarios/login.html',
                      {'login_form': login_form})
