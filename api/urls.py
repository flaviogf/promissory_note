"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.beneficiarios.viewsets import BeneficiarioViewSet
from api.contas.viewsets import ContaViewSet
from api.emitentes.viewsets import EmitenteViewSet

router = DefaultRouter()
router.register('api/v1/emitentes',
                EmitenteViewSet,
                basename='emitente')
router.register('api/v1/beneficiarios',
                BeneficiarioViewSet,
                basename='beneficiario')
router.register('api/v1/contas',
                ContaViewSet,
                basename='conta')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
