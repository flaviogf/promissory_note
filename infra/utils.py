from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    return Response(status=response.status_code)


def not_found(request, exception):
    return HttpResponse(status=HTTP_404_NOT_FOUND)


def server_error(request):
    return HttpResponse(status=HTTP_500_INTERNAL_SERVER_ERROR)
