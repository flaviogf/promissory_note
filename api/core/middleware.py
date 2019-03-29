from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print('erro', exception)
