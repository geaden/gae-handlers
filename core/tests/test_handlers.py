# -*- coding: utf-8 -*-

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


import unittest

import webapp2
import webtest

from .test_common import CommonTestCase

from ..base_handler import BaseHandler



class TestHandler(BaseHandler):
    """
    Mock handler
    """
    template_name = 'test_template.html'

    def get_context(self, *args, **kwargs):
        ctx = super(TestHandler, self).get_context(*args, **kwargs)
        ctx['ctx1'] = 'Test Context'
        return ctx


class BaseHandlerTest(CommonTestCase):
    def setUp(self):
        super(BaseHandlerTest, self).setUp()
        # Create a WSGI application.
        app = webapp2.WSGIApplication([
            ('/', TestHandler),
            (r'/(\w+)/?', TestHandler)])
        # Wrap the app with WebTest’s TestApp.
        self.testapp = webtest.TestApp(app)

    def test_base_handler_response(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertIn('Test Handler', response.normal_body)

    def test_base_handler_with_key(self):
        response = self.testapp.get('/testApp')
        self.assertEqual(response.status_int, 200)
        self.assertIn('testApp', response.normal_body)

    def test_base_handler_context(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertIn('Test Context', response.normal_body)


if __name__ == '__main__':
    unittest.main()
