from unittest import TestCase

from http_constants.status import HTTPStatus


class TestHttpStatus(TestCase):
    def test_get_code(self):
        status = HTTPStatus(200)
        self.assert_(status.get_code(), 200)

    def test_get_meaning(self):
        status = HTTPStatus(200)
        self.assert_(status.get_meaning(), "OK")
