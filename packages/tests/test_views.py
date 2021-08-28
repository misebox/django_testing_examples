from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase
from django.test import RequestFactory

from packages import views

def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_requrest(request)
    return request

def add_middeware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_response(request)
    return request


class ComboPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_get_combo_page(self):
        request = self.factory.get('/packages/combos')
        response = views.get_combo_page(request)
        self.assertContains(response, status_code=200, text='package-combo-notfound', count=1)
