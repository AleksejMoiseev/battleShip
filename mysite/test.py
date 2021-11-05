from unittest import skip

import pytest
from rest_framework.test import APIRequestFactory, APITestCase
from  django.urls import reverse

from mysite.views import test3, logger
from books.models import Publisher, Student


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]


@pytest.fixture
def data():
    return 3


def test_new(data):
    assert data == 3

def test_first():
    factory = APIRequestFactory()
    url = reverse('test3')
    request = factory.get(path=url, format='json')
    view= test3
    responce = view(request)
    logger.info(msg=responce.items())
    assert responce.status_code == 200


class StudentTest(APITestCase):

    def setUp(self) -> None:
        Student.objects.create(id=6217, year_in_school='SO')

    def test_so(self):
        responce = self.client.get(reverse('case'))
        self.assertEqual(first=responce.data, second=[{'id': 6217, 'year_in_school': 'SO'}])

    def test_redirect(self):
        response = self.client.get("/test6/")
        self.assertRedirects(response, '/test2/')

    @skip
    def test_so2(self):
        factory = APIRequestFactory()
        url = reverse()
        request = factory.get()
