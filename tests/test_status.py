from unittest import TestCase

from http_constants.status import HttpStatus


class TestHttpStatus(TestCase):
    def test_get_code(self):
        status = HttpStatus(200)
        self.assert_(status.get_code(), 200)

    def test_get_meaning(self):
        status = HttpStatus(200)
        self.assert_(status.get_meaning(), "OK")
