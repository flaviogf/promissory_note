from django.urls import path

from usuarios_api_v1.views import UsuarioViewSet

app_name = 'usuarios_api_v1'

urlpatterns = [
    path('', UsuarioViewSet.as_view({'post': 'create'}), name='create'),
]
