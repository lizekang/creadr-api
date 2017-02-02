#!/usr/bin/env python
# -*- coding: utf-8 -*-

from creadr.app import app
import unittest


class MainTestCase(unittest.TestCase):

    def test_index(self):
        app.testing = True
        client = app.test_client()

        r = client.get('/')
        assert r.status_code == 200
        assert 'Hello World' in r.data.decode('utf-8')
        print 'hello'

if __name__ == '__main__':
    unittest.main()
