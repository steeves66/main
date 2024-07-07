# myapp/middleware.py
import threading

thread_local = threading.local()

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        thread_local.request = request
        response = self.get_response(request)
        return response

    @staticmethod
    def get_request():
        return getattr(thread_local, 'request', None)