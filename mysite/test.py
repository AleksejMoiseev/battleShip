import pytest


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]


@pytest.fixture
def data():
    return 3


def test_new(data):
    assert data == 3
