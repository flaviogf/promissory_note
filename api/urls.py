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
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.beneficiarios.viewsets import BeneficiarioViewSet
from api.emitentes.viewsets import EmitenteViewSet
from api.promissorias.viewsets import PromissoriaViewSet

router = DefaultRouter()

router.register('emitentes', EmitenteViewSet, basename='emitentes')
router.register('beneficiarios', BeneficiarioViewSet, basename='beneficiarios')
router.register('promissorias', PromissoriaViewSet, basename='promissorias')

urlpatterns = [path('admin/', admin.site.urls)] + router.urls
