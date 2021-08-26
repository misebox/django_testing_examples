from django.test import TestCase
from django.urls import reverse


class SimpleViewTestExample(TestCase):

    def setUp(self):
        pass

    def test_hello(self):
        url = reverse('hello_world')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Hello')

